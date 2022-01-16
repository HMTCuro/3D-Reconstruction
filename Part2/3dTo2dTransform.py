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


def writeFaceImage(path1, path2, path3):
    pcd = o3d.io.read_point_cloud(path1)
    print(pcd)

    pts = np.asarray(pcd.points)
    cls = np.asarray(pcd.colors)
    nms = np.asarray(pcd.normals)

    d = []
    for i in range(3):
        d.append(np.mean(nms[:, i]))
    direction = np.array(d)

    pcd0 = o3d.io.read_point_cloud(path2)
    pts0 = np.asarray(pcd0.points)
    cls0 = np.asarray(pcd0.colors)
    nms0 = np.asarray(pcd0.normals)
    pcd0.rotate(getRotateMatrix(direction))

    # o3d.visualization.draw_geometries([pcd1],
    #                                   zoom=0.3412,
    #                                   front=[0, 0, -1],
    #                                   lookat=[0, 0, -1],
    #                                   up=[0, 1, 0])

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

    img = np.zeros([xLength, yLength, 3])
    for i in range(xLength):
        for j in range(yLength):

            if len(matList[i][j]) > 0:
                r = np.mean(cls0[matList[i][j], 0])
                g = np.mean(cls0[matList[i][j], 1])
                b = np.mean(cls0[matList[i][j], 2])
                img[i, j, 0] = r * 255
                img[i, j, 1] = g * 255
                img[i, j, 2] = b * 255
            print('Done (', i, ',', j, ')')
    cv2.imwrite(path3, img)

# writeFaceImage('pointcloud/gym/ground.ply', 'pointcloud/gym/normed_gym.ply', 'images/gym/resultg.png')
# writeFaceImage('pointcloud/gym/east.ply', 'pointcloud/gym/eastface1.ply', 'images/gym/resulte1.png')
# writeFaceImage('pointcloud/gym/east.ply', 'pointcloud/gym/eastface2.ply', 'images/gym/resulte2.png')
# writeFaceImage('pointcloud/gym/west.ply', 'pointcloud/gym/westface1.ply', 'images/gym/resultw1.png')
# writeFaceImage('pointcloud/gym/west.ply', 'pointcloud/gym/westface2.ply', 'images/gym/resultw2.png')
# writeFaceImage('pointcloud/gym/north.ply', 'pointcloud/gym/northface1.ply', 'images/gym/resultn1.png')
# writeFaceImage('pointcloud/gym/north.ply', 'pointcloud/gym/northface2.ply', 'images/gym/resultn2.png')
# writeFaceImage('pointcloud/gym/south.ply', 'pointcloud/gym/southface1.ply', 'images/gym/results1.png')
# writeFaceImage('pointcloud/gym/south.ply', 'pointcloud/gym/southface2.ply', 'images/gym/results2.png')
#
# writeFaceImage('pointcloud/dby/east.ply', 'pointcloud/dby/eastface.ply', 'images/dby/resulte.png')
writeFaceImage('pointcloud/dby/south.ply', 'pointcloud/dby/southface.ply', 'images/dby/results1.png')
# writeFaceImage('pointcloud/dby/north.ply', 'pointcloud/dby/northface.ply', 'images/dby/resultn.png')
