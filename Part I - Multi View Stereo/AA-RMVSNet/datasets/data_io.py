# Reference: https://github.com/QT-Zhu/AA-RMVSNet

import numpy as np
import re
import sys
import struct
import sys
from typing import Dict, List, Tuple

import cv2

from PIL import Image


def read_pfm(filename):
    file = open(filename, 'rb')

    header = file.readline().decode('utf-8').rstrip()
    if header == 'PF':
        color = True
    elif header == 'Pf':
        color = False
    else:
        raise Exception('Not a PFM file.')

    dim_match = re.match(r'^(\d+)\s(\d+)\s$', file.readline().decode('utf-8'))
    if dim_match:
        width, height = map(int, dim_match.groups())
    else:
        raise Exception('Malformed PFM header.')

    scale = float(file.readline().rstrip())
    if scale < 0:  # little-endian
        endian = '<'
        scale = -scale
    else:
        endian = '>'  # big-endian

    data = np.fromfile(file, endian + 'f')
    shape = (height, width, 3) if color else (height, width)

    data = np.reshape(data, shape)
    data = np.flipud(data)
    file.close()
    return data, scale


def save_pfm(filename, image, scale=1):
    file = open(filename, "wb")

    image = np.flipud(image)

    if image.dtype.name != 'float32':
        raise Exception('Image dtype must be float32.')

    if len(image.shape) == 3 and image.shape[2] == 3:  # color image
        color = True
    elif len(image.shape) == 2 or len(image.shape) == 3 and image.shape[2] == 1:  # greyscale
        color = False
    else:
        raise Exception('Image must have H x W x 3, H x W x 1 or H x W dimensions.')

    file.write('PF\n'.encode('utf-8') if color else 'Pf\n'.encode('utf-8'))
    file.write('{} {}\n'.format(image.shape[1], image.shape[0]).encode('utf-8'))

    endian = image.dtype.byteorder

    if endian == '<' or endian == '=' and sys.byteorder == 'little':
        scale = -scale

    file.write(('%f\n' % scale).encode('utf-8'))

    image.tofile(file)
    file.close()


def scale_to_max_dim(image: np.ndarray, max_dim: int) -> Tuple[np.ndarray, int, int]:
    """Scale image to specified max dimension

    Args:
        image: the input image in original size
        max_dim: the max dimension to scale the image down to if smaller than the actual max dimension

    Returns:
        Tuple of scaled image along with original image height and width
    """
    original_height = image.shape[0]
    original_width = image.shape[1]
    scale = max_dim / max(original_height, original_width)
    if 0 < scale < 1:
        width = int(scale * original_width)
        height = int(scale * original_height)
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)

    return image, original_height, original_width


def read_image(filename: str, max_dim: int = -1) -> Tuple[np.ndarray, int, int]:
    """Read image and rescale to specified max dimension (if exists)

    Args:
        filename: image input file path string
        max_dim: max dimension to scale down the image; keep original size if -1

    Returns:
        Tuple of scaled image along with original image height and width
    """
    image = Image.open(filename)
    # scale 0~255 to 0~1
    np_image = np.array(image, dtype=np.float32) / 255.0
    return scale_to_max_dim(np_image, max_dim)


def save_image(filename: str, image: np.ndarray) -> None:
    """Save images including binary mask (bool), float (0<= val <= 1), or int (as-is)

    Args:
        filename: image output file path string
        image: output image array
    """
    if image.dtype == bool:
        image = image.astype(np.uint8) * 255
    elif image.dtype == np.float32 or image.dtype == np.float64:
        image = image * 255
        image = image.astype(np.uint8)
    else:
        image = image.astype(np.uint8)
    Image.fromarray(image).save(filename)


def read_image_dictionary(filename: str) -> Dict[int, str]:
    """Create image dictionary from file; useful for ETH3D dataset reading and conversion.

    Args:
        filename: input dictionary text file path

    Returns:
        Dictionary of image id (int) and corresponding image file name (string)
    """
    image_dict: Dict[int, str] = {}
    with open(filename) as f:
        num_entries = int(f.readline().strip())
        for _ in range(num_entries):
            parts = f.readline().strip().split(' ')
            image_dict[int(parts[0].strip())] = parts[1].strip()
    return image_dict


# TODO: checked
def read_cam_file(filename, interval_scale):
    """Read camera intrinsics, extrinsics, and depth values (min, max) from text file

    Args:
        filename: cam text file path string
        interval_scale:
    Returns:
        Tuple with intrinsics matrix (3x3), extrinsics matrix (4x4), and depth params vector (min and max) if exists
    """
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]
    # extrinsics: line [1,5), 4x4 matrix
    extrinsics = np.fromstring(' '.join(lines[1:5]), dtype=np.float32, sep=' ').reshape((4, 4))
    # intrinsics: line [7-10), 3x3 matrix
    intrinsics = np.fromstring(' '.join(lines[7:10]), dtype=np.float32, sep=' ').reshape((3, 3))
    # depth min & depth_interval: line 11
    depth_min = float(lines[11].split()[0])
    depth_interval = float(lines[11].split()[1]) * interval_scale
    return intrinsics, extrinsics, depth_min, depth_interval


def read_pair_file(filename: str) -> List[Tuple[int, List[int]]]:
    """Read image pairs from text file and output a list of tuples each containing the reference image ID and a list of
    source image IDs

    Args:
        filename: pair text file path string

    Returns:
        List of tuples with reference ID and list of source IDs
    """
    data = []
    with open(filename) as f:
        num_viewpoint = int(f.readline())
        for _ in range(num_viewpoint):
            ref_view = int(f.readline().rstrip())
            src_views = [int(x) for x in f.readline().rstrip().split()[1::2]]
            if len(src_views) != 0:
                data.append((ref_view, src_views))
    return data


def read_map(path: str, max_dim: int = -1) -> np.ndarray:
    """ Read a binary depth map from either PFM or Colmap (bin) format determined by the file extension and also scale
    the map to the max dim if given

    Args:
        path: input depth map file path string
        max_dim: max dimension to scale down the map; keep original size if -1

    Returns:
        Array of depth map values
    """
    if path.endswith('.bin'):
        in_map = read_bin(path)
    elif path.endswith('.pfm'):
        in_map, _ = read_pfm(path)
    else:
        raise Exception('Invalid input format; only pfm and bin are supported')
    return scale_to_max_dim(in_map, max_dim)[0]


def save_map(path: str, data: np.ndarray) -> None:
    """Save binary depth or confidence maps in PFM or Colmap (bin) format determined by the file extension

    Args:
        path: output map file path string
        data: map data array
    """
    if path.endswith('.bin'):
        save_bin(path, data)
    elif path.endswith('.pfm'):
        save_pfm(path, data)
    else:
        raise Exception('Invalid input format; only pfm and bin are supported')


def read_bin(path: str) -> np.ndarray:
    """Read a depth map from a Colmap .bin file

    Args:
        path: .pfm file path string

    Returns:
        data: array of shape (H, W, C) representing loaded depth map
    """
    with open(path, 'rb') as fid:
        width, height, channels = np.genfromtxt(fid, delimiter='&', max_rows=1,
                                                usecols=(0, 1, 2), dtype=int)
        fid.seek(0)
        num_delimiter = 0
        byte = fid.read(1)
        while True:
            if byte == b'&':
                num_delimiter += 1
                if num_delimiter >= 3:
                    break
            byte = fid.read(1)
        data = np.fromfile(fid, np.float32)
    data = data.reshape((width, height, channels), order='F')
    data = np.transpose(data, (1, 0, 2))
    return data


def save_bin(filename: str, data: np.ndarray):
    """Save a depth map to a Colmap .bin file

    Args:
        filename: output .pfm file path string,
        data: depth map to save, of shape (H,W) or (H,W,C)
    """
    if data.dtype != np.float32:
        raise Exception('Image data type must be float32.')

    if len(data.shape) == 2:
        height, width = data.shape
        channels = 1
    elif len(data.shape) == 3 and (data.shape[2] == 3 or data.shape[2] == 1):
        height, width, channels = data.shape
    else:
        raise Exception('Image must have H x W x 3, H x W x 1 or H x W dimensions.')

    with open(filename, 'w') as fid:
        fid.write(str(width) + '&' + str(height) + '&' + str(channels) + '&')

    with open(filename, 'ab') as fid:
        if len(data.shape) == 2:
            image_trans = np.transpose(data, (1, 0))
        else:
            image_trans = np.transpose(data, (1, 0, 2))
        data_1d = image_trans.reshape(-1, order='F')
        data_list = data_1d.tolist()
        endian_character = '<'
        format_char_sequence = ''.join(['f'] * len(data_list))
        byte_data = struct.pack(endian_character + format_char_sequence, *data_list)
        fid.write(byte_data)

