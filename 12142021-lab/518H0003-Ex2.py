"""
Name: 518H0003-Ex2.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 14/12/2021 16:30
Desc:
"""
import os

import cv2
import numpy as np


def canny(lane_image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


def region_of_interest(image):
    polygons = np.array([
        [(50, 270), (220, 160), (360, 160), (480, 270)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image



files = os.listdir('frames')

for f in files:
    image = cv2.imread('frames/' + f)
    lane_image = np.copy(image)

    canny_image = canny(lane_image)
    cropped_image = region_of_interest(canny_image)

    lines = cv2.HoughLinesP(cropped_image, 1, np.pi / 180, 30, np.array([]), maxLineGap=4)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(lane_image, (x1, y1), (x2, y2), (255, 0, 0), 3)

    cv2.imshow('result', lane_image)
    cv2.waitKey(0)

