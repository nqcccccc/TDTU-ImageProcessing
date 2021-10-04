"""
Name: 518H0003-Ex4.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 03/10/2021 18:19
Desc:
"""
import cv2

img = cv2.imread('lena.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(img, 'Ex4', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_04.png', img)