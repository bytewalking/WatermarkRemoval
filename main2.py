import cv2
import numpy as np
path = "test_image.jpg"

img = cv2.imread(path)
height, width = img.shape[0:2]
print('raw_height:{},raw_width:{}'.format(height, width))

# 计算操作区域
# 右下角
h_start = height-40
h_end = height
w_start = width-130
w_end = width

# 开始操作
copy_img = img[h_start:h_end, w_start:w_end]
height, width = copy_img.shape[0:2]
print('height:{},width:{}'.format(height, width))

thresh = cv2.inRange(copy_img, np.array([200, 200, 200]), np.array([255, 255, 255]))
scan = np.ones((3, 3), np.uint8)
cor = cv2.dilate(thresh, scan, iterations=1)
specular = cv2.inpaint(copy_img, cor, 5, flags=cv2.INPAINT_TELEA)

img[h_start:h_end, w_start:w_end] = specular
# 操作结束，输出图片，展示效果
cv2.namedWindow("image", 0)
cv2.imshow("image", img)

cv2.namedWindow("modified", 0)
cv2.imshow("modified", specular)

cv2.waitKey(0)
cv2.destroyAllWindows()
