"""
Name: demo2.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 14/12/2021 23:10
Desc:
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('img_1.png', 0)

height, width = template.shape[::]

res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
plt.imshow(res, cmap='gray')
plt.show()

loc = np.where( res >= 0.95)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + width, pt[1] + height), (255, 0, 0), 1)

cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()