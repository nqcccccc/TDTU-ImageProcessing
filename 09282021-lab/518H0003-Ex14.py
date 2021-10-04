"""
Name: 518H0003-Ex14.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 03/10/2021 18:48
Desc:
"""
import cv2

img = cv2.imread('lena.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(img, 'Ex14', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow('Ex 14',img)
cv2.waitKey(0)

cv2.imwrite('image_14.png', img)
cv2.destroyAllWindows()