"""
Name: 518H0003-Ex17.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 03/10/2021 18:55
Desc:
"""

import cv2

img = cv2.imread('lena.jpg')

center_coordinates = (400, 400)
axesLength = (100, 50)
angle = 30
startAngle = 0
endAngle = 360
color = (255, 0, 0)
thickness = -1

img = cv2.ellipse(img, center_coordinates, axesLength, angle,
                    startAngle, endAngle, color, thickness)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(img, 'Ex17', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_17.png', img)