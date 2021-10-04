"""
Name: 518H0003-Ex6.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 28/09/2021 16:56
Desc:
"""

import cv2

img1 = cv2.imread('lena1.jpg')
img2 = cv2.imread('lena2.jpg')

weightedSum = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(weightedSum, 'Ex6', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_06.png', img)

cv2.imshow('Weighted Image', weightedSum)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()