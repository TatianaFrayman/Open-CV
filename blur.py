import numpy as np
import cv2

img = cv2.imread("C:/Users/asus/Downloads/Telegram Desktop/noise1.jpg")

kernel = np.array([[0,0,0],
                   [0,2,0],
                   [0,0,0]])
img_up = cv2.filter2D(np.uint8(img), cv2.CV_16U, kernel)
kernel_sub = np.ones((3,3), np.float32)/9

img_res = img_up - img_blur

img_blur = cv2.filter2D(img, -1, kernel_sub)


kernel_res = kernel - kernel_sub
img_res =

np.uint8(img_res)
cv2.imshow('res', img_res)
cv2.waitKey()

