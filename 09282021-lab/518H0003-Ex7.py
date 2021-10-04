"""
Name: 518H0003-Ex7.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 28/09/2021 17:03
Desc:
"""

import cv2

img1 = cv2.imread('lena1.jpg')
img2 = cv2.imread('lena2.jpg')

dest_or = cv2.bitwise_or(img2, img1, mask=None)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(dest_or, 'Ex7', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_07.png', dest_or)

cv2.imshow('Bitwise And', dest_or)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()