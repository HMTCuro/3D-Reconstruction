import cv2
import numpy as np
#中位数滤波
def blur(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if i == 0 or j == 0 or i == img.shape[0] - 1 or j == img.shape[1] - 1: continue
            if img[i, j, 0] == 0 and img[i, j, 1] == 0 and img[i, j, 2] == 0:
                for k in range(3):
                    img[i, j, k] = np.median([img[i - 1, j - 1, k],
                                              img[i - 1, j, k],
                                              img[i - 1, j + 1, k],
                                              img[i, j - 1, k],
                                              img[i, j + 1, k],
                                              img[i + 1, j - 1, k],
                                              img[i + 1, j, k],
                                              img[i - 1, j + 1, k]])
    return img
#东北亚学院
names=["resulte","resultn","results"]
for name in names:
    print(name)
    img = cv2.imread("imgs/dby/source/"+name+".png")
    img = blur(img)
    cv2.imwrite("imgs/dby/completion/"+name+".png", img)
#体育馆
# names=["resulte1","resulte2","resultw1","resultw2","results1","results2","resultn1","resultn2"]
# for name in names:
#     print(name)
#     img = cv2.imread("imgs/gym/source/"+name+".png")
#     img = blur(img)
#     cv2.imwrite("imgs/gym/completion/"+name+".png", img)
