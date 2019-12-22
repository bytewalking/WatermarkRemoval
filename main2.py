import cv2
import os
import numpy as np


def do_remove(img, h_start, h_end, w_start, w_end):
    # 开始操作
    copy_img = img[h_start:h_end, w_start:w_end]

    num = 0
    for i in copy_img:
        if [255, 255, 255] in i:
            num = num+1

    if num < 0:
        return img

    thresh = cv2.inRange(copy_img, np.array([150, 150, 150]), np.array([255, 255, 255]))
    scan = np.ones((3, 3), np.uint8)
    cor = cv2.dilate(thresh, scan, iterations=1)
    specular = cv2.inpaint(copy_img, cor, 5, flags=cv2.INPAINT_TELEA)

    img[h_start:h_end, w_start:w_end] = specular

    return img


def remove_water_mark(image_name, image_root, save_root, ):
    if '.gif' in image_name:
        return
    print(os.path.join(image_root, image_name))
    img = cv2.imread(os.path.join(image_root, image_name))
    height, width = img.shape[0:2]
    # 计算操作区域
    # 右下角
    h_start = int(height - height*0.07)
    h_end = height
    w_start = int(width - width*0.30)
    w_end = width
    img = do_remove(img, h_start, h_end, w_start, w_end)

    # 正下方
    h_start = int(height - height * 0.07)
    h_end = height
    w_start = int(width - width * 0.75)
    w_end = int(width - width * 0.45)
    img = do_remove(img, h_start, h_end, w_start, w_end)

    # 正中间
    h_start = int(height - height/2 - (height * 0.03))
    h_end = int(height - height/2 + (height * 0.03))
    w_start = int(width - width * 0.80)
    w_end = int(width - width * 0.25)
    img = do_remove(img, h_start, h_end, w_start, w_end)

    # 保存图片
    filename = os.path.join(save_root, image_name)
    cv2.imwrite(filename, img)


# 遍历文件
file_root = ""
img_files = []
for root, dirs, files in os.walk("/Users/cheney/WorkSpace/WatermarkRemoval/img/weibo"):
    file_root = root  # 当前目录路径
    img_files = files  # 当前路径下所有非目录子文件

for img_name in img_files:
    remove_water_mark(img_name, file_root, "/Users/cheney/WorkSpace/WatermarkRemoval/img/m_weibo")



# # 操作结束，输出图片，展示效果
# cv2.namedWindow("image", 0)
# cv2.imshow("image", img)
#
# cv2.namedWindow("modified", 0)
# cv2.imshow("modified", specular)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
