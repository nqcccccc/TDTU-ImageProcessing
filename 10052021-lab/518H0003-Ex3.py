"""
Name: 518H0003-Ex3.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 05/10/2021 21:19
Desc:
"""
import numpy as np
import cv2


def track(x):
    pass

cv2.namedWindow('HSV')
cv2.resizeWindow('HSV',700,512)
cv2.createTrackbar('H_min', 'HSV', 0, 179, track)
cv2.createTrackbar('S_min', 'HSV', 0, 255, track)
cv2.createTrackbar('V_min', 'HSV', 0, 255, track)

cv2.createTrackbar('H_max', 'HSV', 179, 179, track)
cv2.createTrackbar('S_max', 'HSV', 255, 255, track)
cv2.createTrackbar('V_max', 'HSV', 255, 255, track)

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hmin = cv2.getTrackbarPos('H_min', 'HSV')
    smin = cv2.getTrackbarPos('S_min', 'HSV')
    vmin = cv2.getTrackbarPos('V_min', 'HSV')

    hmax = cv2.getTrackbarPos('H_max', 'HSV')
    smax = cv2.getTrackbarPos('S_max', 'HSV')
    vmax = cv2.getTrackbarPos('V_max', 'HSV')

    lower_bound = np.array([hmin, vmin, smin])
    upper_bound = np.array([hmax, vmax, smax])

    cv2.imshow('Frame', frame)

    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Mask',mask)
    cv2.imshow('Result',result)

cap.release()
cv2.destroyAllWindows()
