import numpy as np
import cv2

img = cv2.imread("C:/Users/asus/Desktop/girl.jpg")

img_resized = cv2.resize(img, (700, 900))
img = cv2.resize(img_resized, None, fx = 0.2, fy = 0.2)
matrix = np.array([[1,0,30],
                  [0,1,50]], dtype=np.float32)

img = cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))
cv2.imshow('affine', img)
cv2.waitKey()

matrix = cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 30, 0.5)
img = cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))
cv2.imshow('affine', img)
cv2.waitKey()

img = cv2.flip(img, 1)
cv2.imshow('affine', img)

img = cv2.pyrDown(img)
img = cv2.pyrUp(img)
cv2.imshow('affine', img)

cv2.waitKey()