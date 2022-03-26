"""
Name: 518H0003-Ex3.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 19/10/2021 16:23
Desc:
"""
import cv2
import numpy as np

img = cv2.imread('img_2.png',cv2.IMREAD_GRAYSCALE)

th,dst = cv2.threshold(img,180,255,cv2.THRESH_BINARY_INV)

cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
