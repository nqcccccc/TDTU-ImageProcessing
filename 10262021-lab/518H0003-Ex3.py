"""
Name: 518H0003-Ex3.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 26/10/2021 16:46
Desc:
"""

import cv2
import numpy as np

img = cv2.imread('img_2.png')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, th1 = cv2.threshold(img_grey, 0, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((4, 4), np.uint8)
closing = cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernel)

opening = cv2.morphologyEx(closing, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_CROSS,(2,10)))


contours, hierarchy = cv2.findContours(image=opening, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

image_copy = img.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=1,
                 lineType=cv2.LINE_AA)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 255, 0), 1)

cv2.imshow('bounding digit', image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
