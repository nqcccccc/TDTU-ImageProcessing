"""
Name: 518H0003-Ex11.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 03/10/2021 18:33
Desc:
"""

import cv2

img = cv2.imread('lena.jpg')


edges = cv2.Canny(img,100,100)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(edges, 'Ex11', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_11.png', img)
