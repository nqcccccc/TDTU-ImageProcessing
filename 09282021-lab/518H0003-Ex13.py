"""
Name: 518H0003-Ex13.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 03/10/2021 18:38
Desc:
"""
import cv2
import numpy as np

img = cv2.imread('lena.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])

lower2 = np.array([160, 100, 20])
upper2 = np.array([179, 255, 255])

lower_mask = cv2.inRange(img, lower1, upper1)
upper_mask = cv2.inRange(img, lower2, upper2)

mask = lower_mask + upper_mask

result = cv2.bitwise_and(img, img, mask=mask)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(result, 'Ex13', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_13.png', img)