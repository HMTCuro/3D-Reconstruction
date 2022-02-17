from PIL import Image, ImageDraw
import numpy as np
import cv2

t2val = {}
font = cv2.FONT_HERSHEY_SIMPLEX
def angle_cos(p0, p1, p2):
    d1, d2 = (p0 - p1).astype('float'), (p2 - p1).astype('float')
    return abs(np.dot(d1, d2) / np.sqrt(np.dot(d1, d1) * np.dot(d2, d2)))
def find_squares(img,min_area,canny_low,canny_high,index_0,cnt_len_num,sum_area):
    squares = []
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # img = cv2.GaussianBlur(img, (3, 3), 0)
    # img = cv2.medianBlur(img, 5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(two_value_dir,gray)
    # cv2.imshow("nusd",gray)
    # cv2.waitKey(0)
    bin = cv2.Canny(gray,canny_low,canny_high)
    # cv2.imshow("nusd",bin)
    # cv2.waitKey(0)
    # cv2.imwrite("imgs/gym/canny/1.png",bin)
    contours, _hierarchy = cv2.findContours(bin, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    index = index_0
    # 轮廓遍历
    for cnt in contours:
        cnt_len = cv2.arcLength(cnt, True)  # 计算轮廓周长
        cnt = cv2.approxPolyDP(cnt, cnt_len_num * cnt_len, True)  # 多边形逼近
        # 条件判断逼近边的数量是否大于等于4，轮廓面积范围，检测轮廓是否为凸的
        if len(cnt) >= 4 and cv2.contourArea(cnt) > min_area and  cv2.contourArea(cnt) < 8000*3 and cv2.isContourConvex(cnt):
            M = cv2.moments(cnt)  # 计算轮廓的矩
            cnt = cnt.reshape(-1, 2)
            sum_area+=cv2.contourArea(cnt)
            index = index + 1
            squares.append(cnt)
    return squares, img,index/2,sum_area/2
def twoValue(image, G):
    for y in range(0, image.size[1]):
        for x in range(0, image.size[0]):
            g = image.getpixel((x, y))
            if g > G:
                t2val[(x, y)] = 1
            else:
                t2val[(x, y)] = 0
def clearNoise(image, N, Z):
    for i in range(0, Z):
        t2val[(0, 0)] = 1
        t2val[(image.size[0] - 1, image.size[1] - 1)] = 1
        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                nearDots = 0
                L = t2val[(x, y)]
                if L == t2val[(x - 1, y - 1)]:
                    nearDots += 1
                if L == t2val[(x - 1, y)]:
                    nearDots += 1
                if L == t2val[(x - 1, y + 1)]:
                    nearDots += 1
                if L == t2val[(x, y - 1)]:
                    nearDots += 1
                if L == t2val[(x, y + 1)]:
                    nearDots += 1
                if L == t2val[(x + 1, y - 1)]:
                    nearDots += 1
                if L == t2val[(x + 1, y)]:
                    nearDots += 1
                if L == t2val[(x + 1, y + 1)]:
                    nearDots += 1
                if nearDots < N:
                    t2val[(x, y)] = 1
def saveImage(filename,size):
    image = Image.new("1", size)
    draw = ImageDraw.Draw(image)
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            draw.point((x, y), t2val[(x, y)])
    image.save(filename)
    return image
def show_img(names,img):
    cv2.imshow(names, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def find_windows(image_dir,source_image_dir,min_area,write_name,canny_low,canny_high,index_0,cnt_len_num,G,sum_area):
    image = Image.open(image_dir).convert("L")
    twoValue(image, G)
    clearNoise(image, 2, 1)
    saveImage("tmp.png",image.size)
    img=cv2.imread("tmp.png")
    img_median = cv2.medianBlur(img, 5)
    source_image=cv2.imread(source_image_dir)
    squares, img_median,index,area = find_squares(img_median,min_area,canny_low,canny_high,index_0,cnt_len_num,sum_area)
    print("窗户数量:"+str(round(index)))
    print("窗户面积:"+str(round(area)*0.00355961390625))#东北亚为0.005*0.005*11.9325*11.9325=0.00355961390625;
                                                       # 体育馆为0.005*0.005*22.064405*22.064405=0.012170949200100627
    cv2.drawContours(source_image, squares, -1, (0, 0, 255), 2)
    cv2.imwrite(write_name,source_image)
    # cv2.imshow('find_windows', source_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
index_0 = 0
#体育馆
# names=["resulte1","resulte2","resultw1","resultw2","results1","results2","resultn1","resultn2"]
# for name in names:
#     print(name)
#     find_windows(image_dir="imgs/gym/two-value/"+name+".png",
#                  source_image_dir="imgs/gym/completion/"+name+".png",
#                  min_area=110,
#                  write_name="imgs/gym/results/"+name+"_processed.png",
#                  canny_low=50,
#                  canny_high=170,
#                  index_0=0,
#                  cnt_len_num=0.02,
#                  G=100,
#                  sum_area=0)
#东北亚学院
names=["resulte","results","resultn"]
for name in names:
    print(name)
    find_windows(image_dir="imgs/dby/two-value/"+name+".png",
                 source_image_dir="imgs/dby/completion/"+name+".png",
                 min_area=50,
                 write_name="imgs/dby/results/"+name+"_processed.png",
                 canny_low=80,
                 canny_high=170,
                 index_0=0,
                 cnt_len_num=0.02,
                 G=100,
                 sum_area=0)