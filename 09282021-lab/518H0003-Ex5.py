"""
Name: 518H0003-Ex5.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 28/09/2021 16:54
Desc:
"""

import cv2

img = cv2.imread('lena.jpg')
B, G, R = cv2.split(img)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

B = cv2.putText(B, 'Ex5', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_05.png', B)

cv2.imshow("original", img)
cv2.waitKey(0)

cv2.imshow("blue", B)
cv2.waitKey(0)

cv2.imshow("Green", G)
cv2.waitKey(0)

cv2.imshow("red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()