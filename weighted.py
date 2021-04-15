import numpy as np
import cv2


img_1 = cv2.imread("C:/Users/asus/Downloads/Telegram Desktop/car_add.jpg")
img_2 = cv2.imread("C:/Users/asus/Downloads/Telegram Desktop/road_add.jpg")

img_res = cv2.addWeighted(img_1, 0.5, img_2, 0.7, 0)
cv2.imshow('res', img_res)
cv2.waitKey()