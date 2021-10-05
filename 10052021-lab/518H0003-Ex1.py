"""
Name: 518H0003-Ex1.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 05/10/2021 16:14
Desc:
"""
import cv2
import numpy as np

img = cv2.imread('balloon.png')

# Ex1
(B,G,R) = cv2.split(img)

zeros = np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow('Red', cv2.merge([zeros, zeros, R]))
cv2.imshow('Green', cv2.merge([zeros, G, zeros]))
cv2.imshow('Blue', cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()

# #Ex2
color = (100, 100, 100)
thickness = 5
start_point = [(68, 15),(250,100),(400,25),(585,100),(750,30)]
end_point = [(215 , 200),(355,260),(550,221),(730,280),(900,211)]

for i in range(len(start_point)):
    img_rec = cv2.rectangle(img, start_point[i], end_point[i], color, thickness)

cv2.imshow('Rectangle',img_rec)

cv2.waitKey(0)
cv2.destroyAllWindows()

# #Ex3
font = cv2.FONT_HERSHEY_SIMPLEX
org = [(68, 15),(250,100),(400,25),(585,100),(750,30)]
fontScale = 1
color = [(0,255,255),(255,0,0),(0,0,255),(0,255,0),(0,165,255)]
thickness = 2
text = ['yellow','blue','red','green','orange']

for i in range(len(start_point)):
    img_text = cv2.putText(img_rec, text[i], org[i], font,fontScale, color[i], thickness, cv2.LINE_AA)

cv2.imshow('Text above boundary',img_text)

cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('balloon.png')

#Ex4
yellow = img[15:200,65:215]

cv2.imshow('Yellow balloon',yellow)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Ex5

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower1 = np.array([20, 100, 100])
upper1 = np.array([30, 255, 255])

mask = cv2.inRange(img_hsv, lower1, upper1)

result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Yellow balloon hsv',result)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Ex6

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower1 = np.array([20, 100, 100])
upper1 = np.array([30, 255, 255])

mask = cv2.inRange(img_hsv, lower1, upper1)

img[mask>0]=(0,139,0)

cv2.imshow('Change yellow balloon to green',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('balloon.png')
#Ex7
img_crop = img[15:500,65:220]
(rows, cols) = img_crop.shape[:2]

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 20, 1)
img_crop = cv2.warpAffine(img_crop, M, (cols, rows))

cv2.imshow('Rotate 1st balloon',img_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()