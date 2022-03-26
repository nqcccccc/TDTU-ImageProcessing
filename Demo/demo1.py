"""
Name: demo1.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 14/12/2021 23:09
Desc:
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('img_1.png', 0)

height, width = template.shape[::]

res = cv2.matchTemplate(gray, template, cv2.TM_SQDIFF)
plt.imshow(res, cmap='gray')
plt.show()

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = min_loc
print(top_left)
bottom_right = (top_left[0] + width, top_left[1] + height)
cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)

cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()