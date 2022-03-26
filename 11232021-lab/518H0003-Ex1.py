"""
Name: 518H0003-Ex1.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 23/11/2021 16:29
Desc:
"""
import math

import cv2
import numpy as np

img = cv2.imread('img.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)

canny = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
cv2.imshow('Canny Edge Detection', canny)

houghLines = cv2.HoughLines(canny, 1, np.pi / 180, 150, None, 0, 0)
if houghLines is not None:
        for i in range(0, len(houghLines)):
            rho = houghLines[i][0][0]
            theta = houghLines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(img_gray, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)

cv2.imshow('Hough Lines Detection', img_gray)




cv2.imwrite('Sobel_edge_detection.png',sobelxy)
cv2.imwrite('Canny_edge_detection.png',canny)
cv2.imwrite('Hough_line.png',img_gray)

img = cv2.imread('img_1.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
rows = img_blur.shape[0]
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, rows / 8,
                          param1=100, param2=30,
                          minRadius=1, maxRadius=30)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        cv2.circle(img, center, 1, (0, 100, 100), 3)
        radius = i[2]
        cv2.circle(img, center, radius, (255, 0, 255), 3)

cv2.imshow("Hough circles", img)
cv2.imwrite('Hough_circle.png',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
