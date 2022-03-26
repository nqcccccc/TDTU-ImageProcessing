"""
Name: 518H0003-Ex2.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 19/10/2021 16:18
Desc:
"""

import cv2
import numpy as np

img1 = cv2.imread('img.png')
img2 = cv2.imread('img_1.png')

img2 = cv2.resize(img2,img1.shape[1::-1])

dst = cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('Blended',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
