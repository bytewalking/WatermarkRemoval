import cv2
import numpy as np
path = "test_img2.jpg"

img = cv2.imread(path)
height,width = img.shape[0:2]
#開始操作
thresh = cv2.inRange( img,np.array([230, 230, 230]), np.array([255, 255, 255]) )
scan = np.ones( (3,3),np.uint8)
cor = cv2.dilate(thresh,scan,iterations=1)
specular = cv2.inpaint(img,cor,5,flags=cv2.INPAINT_TELEA)

#操作結束，下面開始是輸出圖片的代碼
cv2.namedWindow("image",0)
cv2.imshow("image",img)

cv2.namedWindow("modified",0)
cv2.imshow("modified",specular)

cv2.waitKey(0)
cv2.destroyAllWindows()