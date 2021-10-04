"""
Name: 518H0003-Ex16.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 03/10/2021 18:51
Desc:
"""
import cv2

img = cv2.imread('lena.jpg')

start_point = (200, 200)
end_point = (900, 250)
color = (125, 100, 100 )

thickness = 9

img = cv2.arrowedLine(img, start_point, end_point, color, thickness)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

img = cv2.putText(img, 'Ex16', org, font,fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite('image_16.png', img)


