"""
Name: 518H0003-EX18.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 03/10/2021 18:58
Desc:
"""

import cv2

img = cv2.imread('lena.jpg')

center = (400, 400)
radius = 50
angle = 30
color = (255, 0, 0)
thickness = 10

img = cv2.circle(img,center,radius,color,thickness)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(img, 'Ex18', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_18.png', img)