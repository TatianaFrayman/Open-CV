import numpy as np
import cv2

#img = cv2.imread('C:/Users/asus/Downloads/Telegram Desktop/spoons.png', 0)
img = cv2.imread('C:/Users/asus/Downloads/Telegram Desktop/paper.png', 0)
img_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 1, 0)

#ret, img_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('thresh', img_thresh)
cv2.waitKey()