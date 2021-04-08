import numpy as np
import cv2 as cv
import cv2

negative_image = cv2.imread('C:/Users/asus/Desktop/girl.jpg')
(h, w) = negative_image.shape[:2]
colorfull = np.zeros(negative_image.shape, dtype=np.uint8)
#for y in range(h):
#    for x in range(w):
#        b = negative_image[y, x, 0]
#        g = negative_image[y, x, 1]
#        r = negative_image[y, x, 2]
#        colorfull[y,x] = (255-b, 255-g, 255-r)

colorfull = 255 - negative_image

cv2.imshow('result', colorfull)
cv2.waitKey()