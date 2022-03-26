"""
Name: 518H0003-Ex1.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 19/10/2021 16:03
Desc:
"""
import cv2
import numpy as np

img = cv2.imread('img.png')

mask = np.zeros(img.shape[:2],dtype='uint8')

cv2.circle(mask,(250,365),140,255,-1)
cv2.circle(mask,(730,280),140,255,-1)
cv2.circle(mask,(1170,410),140,255,-1)

masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('Three faces',masked)

cv2.waitKey(0)
cv2.destroyAllWindows()