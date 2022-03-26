"""
Name: 518H0003-Ex2.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 26/10/2021 15:54
Desc:
"""
import cv2
import numpy as np

img = cv2.imread('img_1.png')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, th1 = cv2.threshold(img_grey, 1, 255, cv2.THRESH_BINARY_INV)

dilation = cv2.dilate(th1, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4)), iterations=1)
opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT,(10,10)))

contours, hierarchy = cv2.findContours(image=opening, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

image_copy = img.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=1,
                 lineType=cv2.LINE_AA)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 255, 0), 1)

cv2.imshow('Bounding number', image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
