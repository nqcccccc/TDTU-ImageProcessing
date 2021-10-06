"""
Name: 518H0003-Ex2.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 05/10/2021 20:15
Desc:
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

cv2.imwrite('ouput.png',frame)

# Ex 8
img = cv2.imread('ouput.png')

ins = cv2.add(img, 20)

res = np.hstack((img, ins))

cv2.imshow('Brightness Increase', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ex9
img = cv2.imread('ouput.png')

R, G, B = cv2.split(img)

output1_R = cv2.equalizeHist(R)
output1_G = cv2.equalizeHist(G)
output1_B = cv2.equalizeHist(B)

equ = cv2.merge((output1_R, output1_G, output1_B))

res = np.hstack((img, equ))

cv2.imshow('Global histogram equalization ', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Ex 10
img = cv2.imread('ouput.png')

R, G, B = cv2.split(img)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

output1_R = clahe.apply(R)
output1_G = clahe.apply(G)
output1_B = clahe.apply(B)

equ = cv2.merge((output1_R, output1_G, output1_B))

res = np.hstack((img, equ))

cv2.imshow('Adaptive histogram equalization', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
