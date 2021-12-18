import open3d as o3d
import numpy as np
import cmath
import cv2


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


def getWindowsList(path1, path2, path3):
    pcd = o3d.io.read_point_cloud(path1)
    print(pcd)

    nms = np.asarray(pcd.normals)

    d = []
    for i in range(3):
        d.append(np.mean(nms[:, i]))
    direction = np.array(d)

    pcd0 = o3d.io.read_point_cloud(path2)
    pts0 = np.asarray(pcd0.points)
    pts1 = np.array(pts0)

    pcd0.rotate(getRotateMatrix(direction))

    lMargin = np.min(pts0[:, 0])
    rMargin = np.max(pts0[:, 0])
    tMargin = np.max(pts0[:, 1])
    bMargin = np.min(pts0[:, 1])

    print(lMargin, rMargin, tMargin, bMargin)

    step = 0.005
    xLength = int((rMargin - lMargin) / step) + 1
    yLength = int((tMargin - bMargin) / step) + 1
    print(xLength, yLength)

    matList = []
    for i in range(xLength):
        v = []
        for j in range(yLength):
            v.append([])
        matList.append(v)

    for i in range(pts0.shape[0]):
        matList[int((pts0[i, 0] - lMargin) / step)][int((tMargin - pts0[i, 1]) / step)].append(i)

    windowList = []
    img = cv2.imread(path3)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if np.all(img[i, j] == np.array([0, 0, 0])):
                for k in range(len(matList[i][j])):
                    windowList.append(matList[i][j][k])

    windowList.sort()
    return pts1[windowList, :]


# ptsW = getWindowsList('pointcloud/gym/north.ply', 'pointcloud/gym/northface1.ply', 'images/gym/two-value/resultn1.png')
# ptsW = getWindowsList('pointcloud/gym/north.ply', 'pointcloud/gym/northface2.ply', 'images/gym/two-value/resultn2.png')
# ptsW = getWindowsList('pointcloud/gym/south.ply', 'pointcloud/gym/southface1.ply', 'images/gym/two-value/results1.png')
# ptsW = getWindowsList('pointcloud/gym/south.ply', 'pointcloud/gym/southface2.ply', 'images/gym/two-value/results2.png')
# ptsW = getWindowsList('pointcloud/gym/east.ply', 'pointcloud/gym/eastface1.ply', 'images/gym/two-value/resulte1.png')
# ptsW = getWindowsList('pointcloud/gym/east.ply', 'pointcloud/gym/eastface2.ply', 'images/gym/two-value/resulte2.png')
# ptsW = getWindowsList('pointcloud/gym/west.ply', 'pointcloud/gym/westface1.ply', 'images/gym/two-value/resultw1.png')
# ptsW = getWindowsList('pointcloud/gym/west.ply', 'pointcloud/gym/westface2.ply', 'images/gym/two-value/resultw2.png')
# ptsW = getWindowsList('pointcloud/dby/north.ply', 'pointcloud/dby/northface.ply', 'images/dby/two-value/resultn.png')
ptsW = getWindowsList('pointcloud/dby/south.ply', 'pointcloud/dby/southface.ply', 'images/dby/two-value/results.png')
# ptsW = getWindowsList('pointcloud/dby/east.ply', 'pointcloud/dby/eastface.ply', 'images/dby/two-value/resulte.png')


print(ptsW.shape)
# pcdMain = o3d.io.read_point_cloud('pointcloud/gym/northface1.ply')
# pcdMain = o3d.io.read_point_cloud('pointcloud/gym/northface2.ply')
# pcdMain = o3d.io.read_point_cloud('pointcloud/gym/southface1.ply')
# pcdMain = o3d.io.read_point_cloud('pointcloud/gym/southface2.ply')
# pcdMain = o3d.io.read_point_cloud('pointcloud/gym/eastface1.ply')
# pcdMain = o3d.io.read_point_cloud('pointcloud/gym/eastface2.ply')
# pcdMain = o3d.io.read_point_cloud('pointcloud/gym/westface1.ply')
# pcdMain = o3d.io.read_point_cloud('pointcloud/gym/westface2.ply')
# pcdMain = o3d.io.read_point_cloud('pointcloud/dby/northface.ply')
pcdMain = o3d.io.read_point_cloud('pointcloud/dby/southface.ply')
# pcdMain = o3d.io.read_point_cloud('pointcloud/dby/eastface.ply')

print(pcdMain)

ptsMain = np.asarray(pcdMain.points)
clsMain = np.asarray(pcdMain.colors)

idx = 0
for i in range(ptsMain.shape[0]):
    if np.all(ptsMain[i] == ptsW[idx]):
        idx += 1
        clsMain[i, 0] = 1
        clsMain[i, 1] = 0
        clsMain[i, 2] = 0
        if idx == ptsW.shape[0]:
            break

    if not i % 100000:
        print(i, '/', ptsMain.shape[0])

print(idx, 'of', ptsW.shape[0])
# o3d.io.write_point_cloud('pointcloud/gym/windowsGymn1.ply', pcdMain)
# o3d.io.write_point_cloud('pointcloud/gym/windowsGymn2.ply', pcdMain)
# o3d.io.write_point_cloud('pointcloud/gym/windowsGyms1.ply', pcdMain)
# o3d.io.write_point_cloud('pointcloud/gym/windowsGyms2.ply', pcdMain)
# o3d.io.write_point_cloud('pointcloud/gym/windowsGyme1.ply', pcdMain)
# o3d.io.write_point_cloud('pointcloud/gym/windowsGyme2.ply', pcdMain)
# o3d.io.write_point_cloud('pointcloud/gym/windowsGymw1.ply', pcdMain)
# o3d.io.write_point_cloud('pointcloud/gym/windowsGymw2.ply', pcdMain)
# o3d.io.write_point_cloud('pointcloud/dby/windowsDbyn.ply', pcdMain)
o3d.io.write_point_cloud('pointcloud/dby/windowsDbys.ply', pcdMain)
# o3d.io.write_point_cloud('pointcloud/dby/windowsDbye.ply', pcdMain)
