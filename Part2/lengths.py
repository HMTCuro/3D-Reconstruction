import open3d as o3d
import numpy as np
import cmath


def getRotateMatrix(direction):
    theta = cmath.polar(complex(direction[0], direction[1]))[1]
    phi = np.arccos(direction[2] / np.linalg.norm(direction))
    m1 = np.zeros([3, 3])
    m1[0, 0] = np.cos(-theta)
    m1[0, 1] = -np.sin(-theta)
    m1[1, 0] = np.sin(-theta)
    m1[1, 1] = np.cos(-theta)
    m1[2, 2] = 1
    m2 = np.zeros([3, 3])
    m2[2, 2] = np.cos(-phi)
    m2[2, 0] = -np.sin(-phi)
    m2[0, 2] = np.sin(-phi)
    m2[0, 0] = np.cos(-phi)
    m2[1, 1] = 1
    return np.dot(m2, m1)


def getHeight(path1, path2):
    pcd = o3d.io.read_point_cloud(path1)
    print(pcd)
    pts = np.asarray(pcd.points)
    pcd1 = o3d.io.read_point_cloud(path2)
    nms1 = np.asarray(pcd1.normals)
    d = []
    for i in range(3):
        d.append(np.mean(nms1[:, i]))
    direction = np.array(d)
    pcd.rotate(getRotateMatrix(direction))
    print('Direction:', path2, 'Length:', np.max(pts[:, 2]) - np.min(pts[:, 2]))


getHeight('pointcloud/gym/building1.ply', 'pointcloud/gym/south.ply')
getHeight('pointcloud/gym/building1.ply', 'pointcloud/gym/east.ply')
getHeight('pointcloud/gym/building1.ply', 'pointcloud/gym/ground.ply')
getHeight('pointcloud/gym/building2.ply', 'pointcloud/gym/south.ply')
getHeight('pointcloud/gym/building2.ply', 'pointcloud/gym/east.ply')
getHeight('pointcloud/gym/building2.ply', 'pointcloud/gym/ground.ply')

# getHeight('pointcloud/dby/building.ply', 'pointcloud/dby/south.ply')
# getHeight('pointcloud/dby/building.ply', 'pointcloud/dby/east.ply')
# getHeight('pointcloud/dby/building.ply', 'pointcloud/dby/ground.ply')