"""
Name: 518H0003-Ex15.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 28/09/2021 17:12
Desc:
"""

import cv2

img = cv2.imread('lena.jpg')

start_point = (500, 500)
end_point = (1000, 250)
color = (125, 100, 100 )

thickness = 9

img = cv2.line(img, start_point, end_point, color, thickness)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(img, 'Ex15', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_15.png', img)

cv2.imshow('Image with line', img)
cv2.waitKey(0)

cv2.destroyAllWindows()