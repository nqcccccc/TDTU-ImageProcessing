"""
Name: 518H0003-Ex1.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 28/09/2021 16:39
Desc:
"""

import cv2

img = cv2.imread('lena.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(img, 'Ex1', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_01.png', img)

print(img)