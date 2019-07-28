"""
图片转bmp灰度图
"""
import cv2
imgpath = r"C:\Users\geoge\Desktop\2.bmp"
img = cv2.imread(imgpath)
cv2.imshow("Image",img)
cv2.waitKey(0)
img0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("b.bmp",img0)