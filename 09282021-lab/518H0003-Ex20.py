"""
Name: 518H0003-Ex20.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 03/10/2021 19:00
Desc:
"""

import cv2

img = cv2.imread('lena.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(img, 'Ex20', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_20.png', img)
