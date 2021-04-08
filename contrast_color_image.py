import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("C:/Users/asus/Desktop/lowContrast1.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
img_res = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
both = np.hstack((img, img_res))
cv2.imshow('see what you got', both)
cv2.waitKey()
cv2.destroyAllWindows()