import numpy as np
import cv2

img = cv2.imread('C:/Users/asus/Downloads/Telegram Desktop/spoons_gaps.png')
cv2.imshow('img', img)

matrix = np.ones((3,3), np.uint8)
delation = cv2.dilate(img, matrix, iterations=5)
cv2.imshow('delation', delation)

erose = cv2.erode(img, matrix, anchor=(0,0))
cv2.imshow('erosion', erose)

cv2.waitKey()