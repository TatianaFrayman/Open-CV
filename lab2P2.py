import numpy as np
import cv2

image_black = np.zeros((480, 640), dtype = np.uint8)
image_color = np.ones((480,640,3), dtype = np.uint8)

height, wight = image_color.shape[:2]

image_color[0:height//2, :, (0, 0)] = 200
image_color[height//2 : height, :, (1, 2)] = 200

cv2.imshow('color_image', image_color)
cv2.waitKey()