import numpy as np
import cv2

img = cv2.imread("C:/Users/asus/Downloads/Telegram Desktop/noise2.jpg")

img_gauss = cv2.GaussianBlur(img, (5,5), None, None)
img_median = cv2.medianBlur(img, 3)


cv2.imshow("Gaussian", img_gauss)
cv2.imshow("Median", img_median)
cv2.waitKey()



