import open3d as o3d
import numpy as np
import cmath


def areaOfSlice(list0):
    if len(list0) == 0:
        return 0
    step2 = 0.02
    start1 = np.min(pts[list0, 1])
    end1 = np.max(pts[list0, 1])
    slice2 = int((end1 - start1) / step2) + 1
    zMin = np.min(pts[list0, 2])
    area = 0

    sliceList1 = []
    for i in range(slice2):
        sliceList1.append([])
    for pt in list0:
        sliceList1[int((pts[pt, 1] - start1) / step2)].append(pt)

    for i in range(slice2):
        if len(sliceList1[i]) == 0:
            continue
        area += step2 * (np.max(pts[sliceList1[i], 2]) - zMin)
    return area


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


# pcd = o3d.io.read_point_cloud("pointcloud/gym/building1.ply")
pcd = o3d.io.read_point_cloud("pointcloud/gym/building2.ply")
# pcd = o3d.io.read_point_cloud("pointcloud/dby/building.ply")
# pcd = o3d.io.read_point_cloud("pointcloud/gym/gym_1024 - Cloud - Cloud.ply")
print(pcd)

pts = np.asarray(pcd.points)
# pcd0 = o3d.io.read_point_cloud("pointcloud/dby/ground.ply")
pcd0 = o3d.io.read_point_cloud("pointcloud/gym/ground.ply")
nms = np.asarray(pcd0.normals)
d = []
for i in range(3):
    d.append(np.mean(nms[:, i]))
direction = np.array(d)

pcd.rotate(getRotateMatrix(direction))

step1 = 0.02
start = np.min(pts[:, 0])
end = np.max(pts[:, 0])

slice1 = int((end - start) / step1) + 1

volume = 0

sliceList = []
for i in range(slice1):
    sliceList.append([])
for pt in range(pts.shape[0]):
    sliceList[int((pts[pt, 0] - start) / step1)].append(pt)
for i in range(slice1):
    volume += areaOfSlice(sliceList[i]) * step1
    print('Done (', i + 1, 'of', slice1, ')')
print('volume=', volume)
