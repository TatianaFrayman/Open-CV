import numpy as np
import cv2

img = cv2.imread('C:/Users/asus/Downloads/Telegram Desktop/spoons_gaps.png')
cv2.imshow('img', img)

matrix = np.ones((7,7), np.uint8)
delation = cv2.dilate(img, matrix, iterations=1)
cv2.imshow('delation', delation)

erose = cv2.erode(img, matrix, anchor=(0,0))
cv2.imshow('erosion', erose)

close_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, matrix)
cv2.imshow('morphology', close_img)
cv2.waitKey()
cv2.destroyAllWindows()