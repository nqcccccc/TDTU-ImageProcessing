"""
Name: 518H0003-Ex8.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 03/10/2021 18:25
Desc:
"""
import cv2

img = cv2.imread('lena.jpg')
# Loading the image

resize = cv2.resize(img,(0,0),fx=0.1,fy=0.1)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (10, 15)
fontScale = 0.5
color = (255, 0, 0)
thickness = 1

img = cv2.putText(resize, 'Ex8', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_08.png', img)
