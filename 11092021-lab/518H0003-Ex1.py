"""
Name: 518H0003-Ex1.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 09/11/2021 15:36
Desc:
"""
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img.png',0)

plt.figure(figsize=(6,5))
plt.title('Histogram for this image in grayscale')
plt.hist(img.ravel(),256,[0,256])
plt.show()

equ = cv2.equalizeHist(img)

plt.figure(figsize=(6,5))
plt.title('Histogram for this image in grayscale after equalization')
plt.hist(equ.ravel(),256,[0,256])
plt.show()

cv2.imshow('Before',img)
cv2.imshow('After',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()