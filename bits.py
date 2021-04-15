import  numpy as np
import cv2

h, w = 480, 480
img_square = np.zeros((h, w), dtype = np.uint8)
cv2.rectangle(img_square, (w//2, h//2), (w,0), 255, -1)
cv2.imshow('rect', img_square)

img_circle = np.zeros((h, w), dtype = np.uint8)
cv2.circle(img_circle, (h//2, w//2), h//2, 255, -1)
cv2.imshow('circ', img_circle)
cv2.waitKey()

result_and = cv2.bitwise_and(img_square, img_circle)
result_or = cv2.bitwise_or(img_square, img_circle)
result_xor = cv2.bitwise_xor(img_square, img_circle)
result_inv = cv2.bitwise_not(img_square, img_circle)

cv2.imshow('and', result_and)
cv2.waitKey()
cv2.imshow('or', result_or)
cv2.waitKey()
cv2.imshow('xor', result_xor)
cv2.waitKey()
cv2.imshow('inverse', result_inv)
cv2.waitKey()

