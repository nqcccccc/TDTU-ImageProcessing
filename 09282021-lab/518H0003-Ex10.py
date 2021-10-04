"""
Name: 518H0003-Ex10.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 28/09/2021 17:10
Desc:
"""

import cv2

img = cv2.imread('lena.jpg',0)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(img, 'Ex10', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_10.png', img)

cv2.imshow('Image test', img)
cv2.waitKey(0)

cv2.destroyAllWindows()