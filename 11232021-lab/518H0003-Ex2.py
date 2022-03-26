"""
Name: 518H0003-Ex2.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 23/11/2021 16:46
Desc:
"""
import cv2
import numpy as np

img = cv2.imread('img.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (11,11), 0)

outer_box = np.zeros(img_blur.shape,np.uint8)

outer_box = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)

outer_box = cv2.bitwise_not(outer_box)

outer_box = cv2.dilate(outer_box,cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3)))

canny = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
cv2.imshow('Canny Edge Detection', outer_box)



count = 0
max = -1
h, w = outer_box.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
maxPt = (0,0)

for y in range(0,outer_box.shape[0]):
    for x in range(0,outer_box.shape[1]):
        if outer_box[y,x] >= 128:
            area = cv2.floodFill(outer_box,mask, seedPoint=(x,y),newVal=64)
            print(area)

            if max == -1:
                maxPt = (x, y)
                max = area

            if area > max:
                maxPt = (x,y)
                max = area

cv2.floodFill(outer_box,mask, seedPoint=maxPt, newVal=255)
for y in range(0,outer_box.shape[0]):
    for x in range(0,outer_box.shape[1]):
        if outer_box[y,x] == 64 and x!= maxPt and y != maxPt:
            area = cv2.floodFill(outer_box,mask, seedPoint=(x,y),newVal=0)

outer_box = cv2.erode(outer_box, cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3)))
cv2.imshow("thresholded", outer_box)

cv2.waitKey(0)
cv2.destroyAllWindows()