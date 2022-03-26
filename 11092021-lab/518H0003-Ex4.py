"""
Name: 518H0003-Ex4.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 09/11/2021 16:08
Desc:
"""

import numpy as np
import cv2

video = cv2.VideoCapture('video.mp4')
frameIds = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)

frames = []
for fid in frameIds:
    video.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = video.read()
    frames.append(frame)

medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)

cv2.imshow('frame', medianFrame)
cv2.waitKey(0)