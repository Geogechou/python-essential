# -*- coding: UTF-8 -*- 
import cv2
import sys
path = ""
if len(sys.argv)>1:
    path=sys.argv[1]
else:
    print("para1 is picture's path")
    exit(-1)
print("path is:"+path)
ori_img = cv2.imread(path)
# 第二个参数，是调整模糊的程度，只能是奇数,越大模糊效果越强
img = cv2.GaussianBlur(ori_img,(99,99),0)
cv2.imwrite("copy.png",img)