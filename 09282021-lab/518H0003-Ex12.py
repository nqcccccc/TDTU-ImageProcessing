"""
Name: 518H0003-Ex12.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 03/10/2021 18:35
Desc:
"""

import cv2

img = cv2.imread('lena.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(img, 'Ex12', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_12.png', img)
