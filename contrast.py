import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("C:/Users/asus/Desktop/lowContrast.jpg", 0)
img_eq = cv2.equalizeHist(img)
both = np.hstack((img, img_eq))
cv2.imshow('see what you got', both)
cv2.waitKey()

