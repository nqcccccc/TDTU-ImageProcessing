"""
Name: 518H0003-Ex2.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 09/11/2021 15:48
Desc:
"""
import cv2
import numpy as np

img = cv2.imread('img.png',0)

noise_img = np.zeros((550, 368))
cv2.randu(noise_img, 0, 256)

noisy_gray = img + np.array(0.2*noise_img, dtype=np.uint8)

kernel = np.ones((5,5),np.float32)/25
img_blur = cv2.filter2D(noisy_gray,-1,kernel)
img_blur_avg = cv2.blur(noisy_gray,ksize=(5,5))
img_blur_guass = cv2.GaussianBlur(noisy_gray,ksize=(5,5),sigmaX=0,sigmaY=0)
img_blur_median = cv2.medianBlur(noisy_gray,ksize=5)
img_blur_bil = cv2.bilateralFilter(noisy_gray,d=9,sigmaColor= 75,sigmaSpace = 75)

cv2.imshow('Before',img)
cv2.imshow('Noise Image',noisy_gray)

cv2.imshow('filter 2D Blur',img_blur)
cv2.imshow('Avg Blur',img_blur_avg)
cv2.imshow('Gaussian Blur',img_blur_guass)
cv2.imshow('Median Blur',img_blur_median)
cv2.imshow('Bilateral Blur',img_blur_bil)
cv2.waitKey(0)
cv2.destroyAllWindows()