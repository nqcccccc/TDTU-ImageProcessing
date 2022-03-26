"""
Name: 518H0003-Ex1.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 26/10/2021 15:46
Desc:
"""
import cv2

img = cv2.imread('img.png',0)

th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,5)

cv2.imshow('ADAPTIVE_THRESH_MEAN_C',th1)

cv2.waitKey(0)
cv2.destroyAllWindows()