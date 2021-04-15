import numpy as np
import cv2

image = cv2.imread("C:/Users/asus/Desktop/girl.jpg")
matrix = np.ones((3,3), dtype = np.float32)
matrix = matrix/9

cv2.imshow("aaa", image)

image_change = cv2.filter2D(image, -1, matrix)
cv2.imshow("gauss", image_change)

cv2.waitKey()