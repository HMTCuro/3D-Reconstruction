from torch.utils.data import Dataset
from .utils import read_pfm
import os
import numpy as np
import cv2
from PIL import Image
import torch
from torchvision import transforms as T


class DTUEvalDataset(Dataset):
    def __init__(self, root_dir, split, n_views=5, levels=3, depth_interval=2.65, img_wh=None):
        """
        img_wh should be set to a tuple ex: (1152, 864) to enable test mode!
        """
        self.root_dir = root_dir
        self.split = split
        assert self.split in ['test', 'test2'], 'split must be "test"!'
        self.img_wh = img_wh
        assert self.img_wh, 'img_wh is None'
        if img_wh is not None:
            assert img_wh[0] % 32 == 0 and img_wh[1] % 32 == 0, 'img_wh must both be multiples of 32!'
        self.build_metas()
        self.n_views = n_views
        self.levels = levels  # FPN levels
        self.depth_interval = depth_interval
        self.build_proj_mats()
        self.define_transforms()

    def build_metas(self):
        self.metas = []
        with open(f'datasets/lists/dtu/{self.split}.txt') as f:
            self.scans = [line.rstrip() for line in f.readlines()]

        # light conditions 0-6 for training
        # light condition 3 for testing (the brightest?)
        light_idxs = [3] if self.img_wh else range(7)

        pair_file = "scan9/pair.txt"
        for scan in self.scans:
            with open(os.path.join(self.root_dir, pair_file)) as f:
                num_viewpoint = int(f.readline())
                # viewpoints (49)
                for _ in range(num_viewpoint):
                    ref_view = int(f.readline().rstrip())
                    src_views = [int(x) for x in f.readline().rstrip().split()[1::2]]
                    for light_idx in light_idxs:
                        self.metas += [(scan, light_idx, ref_view, src_views)]

    def build_proj_mats(self):
        proj_mats = []
        for vid in range(49):  # total 49 view ids
            proj_mat_filename = os.path.join(self.root_dir, f'scan9/cams/{vid:08d}_cam.txt')
            intrinsics, extrinsics, depth_min = self.read_cam_file(proj_mat_filename)
            if self.img_wh is not None:  # resize the intrinsics to the coarsest level
                intrinsics[0] *= self.img_wh[0] / 1600 / 4
                intrinsics[1] *= self.img_wh[1] / 1200 / 4

            # multiply intrinsics and extrinsics to get projection matrix
            proj_mat_ls = []
            for l in reversed(range(self.levels)):
                proj_mat_l = np.eye(4)
                proj_mat_l[:3, :4] = intrinsics @ extrinsics[:3, :4]
                intrinsics[:2] *= 2  # 1/4->1/2->1
                proj_mat_ls += [torch.FloatTensor(proj_mat_l)]
            # (self.levels, 4, 4) from fine to coarse
            proj_mat_ls = torch.stack(proj_mat_ls[::-1])
            proj_mats += [(proj_mat_ls, depth_min)]

        self.proj_mats = proj_mats

    def read_cam_file(self, filename):
        with open(filename) as f:
            lines = [line.rstrip() for line in f.readlines()]
        # extrinsics: line [1,5), 4x4 matrix
        extrinsics = np.fromstring(' '.join(lines[1:5]), dtype=np.float32, sep=' ')
        extrinsics = extrinsics.reshape((4, 4))
        # intrinsics: line [7-10), 3x3 matrix
        intrinsics = np.fromstring(' '.join(lines[7:10]), dtype=np.float32, sep=' ')
        intrinsics = intrinsics.reshape((3, 3))
        # depth_min & depth_interval: line 11
        depth_min = float(lines[11].split()[0])
        return intrinsics, extrinsics, depth_min

    def define_transforms(self):
        self.transform = T.Compose(
            [T.ToTensor(), T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), ])

    def __len__(self):
        return len(self.metas)

    def __getitem__(self, idx):
        sample = {}
        scan, light_idx, ref_view, src_views = self.metas[idx]
        # use only the reference view and first nviews-1 source views
        view_ids = [ref_view] + src_views[:self.n_views - 1]

        imgs = []
        proj_mats = []  # record proj mats between views
        for i, vid in enumerate(view_ids):
            img_filename = os.path.join(self.root_dir, f'scan9/images/{vid:08d}.jpg')

            img = Image.open(img_filename)
            if self.img_wh[0] == 640:
                img = img.resize((800, 600), Image.BILINEAR)  # (600, 800)
                img = np.array(img)[44:556, 80:720]  # (512, 640)
            else:
                img = img.resize(self.img_wh, Image.BILINEAR)
            img = self.transform(img)
            imgs += [img]

            proj_mat_ls, depth_min = self.proj_mats[vid]

            if i == 0:  # reference view
                sample['init_depth_min'] = torch.FloatTensor([depth_min])
                ref_proj_inv = torch.inverse(proj_mat_ls)
            else:
                proj_mats += [proj_mat_ls @ ref_proj_inv]

        imgs = torch.stack(imgs)  # (V, 3, H, W)
        proj_mats = torch.stack(proj_mats)[:, :, :3]  # (V-1, self.levels, 3, 4) from fine to coarse

        sample['imgs'] = imgs
        sample['proj_mats'] = proj_mats
        sample['depth_interval'] = torch.FloatTensor([self.depth_interval])
        sample['scan_vid'] = (scan, ref_view)

        return sample
