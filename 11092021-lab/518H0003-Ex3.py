"""
Name: 518H0003-Ex3.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 09/11/2021 16:03
Desc:
"""
import cv2
import numpy as np

img = cv2.imread('img.png')

smoothed = cv2.GaussianBlur(img, (9, 9), 10)
img_sharp_gauss = cv2.addWeighted(img, 1.5, smoothed, -0.5, 0)

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

img_sharp_2d = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)


cv2.imshow('Before',img)

cv2.imshow('Gaussian Image',img_sharp_gauss)
cv2.imshow('Filter2D Image',img_sharp_2d)
cv2.waitKey(0)
cv2.destroyAllWindows()