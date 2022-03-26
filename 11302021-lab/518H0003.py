"""
Name: 518H0003.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 30/11/2021 15:46
Desc:
"""
import cv2

img = cv2.imread('img.png')

image = img.copy()
img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(img_grey, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
detected_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)

cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    cv2.drawContours(image, [c], -1, (255, 255, 255), 2)

img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret1, th1 = cv2.threshold(img_grey, 0, 255, cv2.THRESH_BINARY_INV)

dilation = cv2.dilate(th1, cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)), iterations=1)
opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_CROSS, (4, 4)))

closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_CROSS, (4, 4)))

contours, hierarchy = cv2.findContours(image=closing, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

image_copy = img.copy()

output = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)
    if area > 100:
        output.append([str(x), str(y), str(w), str(h)])
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 0, 255), 1)

cv2.imwrite('output.jpg', image_copy)

with open('output.txt', 'w') as txt_file:
    for line in output:
        tmp = ' '.join(line)
        txt_file.write(str(tmp) + '\n')
