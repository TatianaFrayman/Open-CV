import numpy as np
import cv2 as cv
import cv2


image_black = np.zeros((480,640), dtype = np.uint8)

cv2.namedWindow('black image', cv2.WINDOW_FULLSCREEN)
cv2.imshow('black image', image_black)

image_from_file = np.zeros((480,640), dtype = np.uint8)
image_from_file = cv2.imread('C:/Users/asus/Desktop/girl.jpg', 0)
(h, w) = image_from_file.shape

print(image_from_file.dtype)
for y in range(h):
    for x in range(w):
        brightness = image_from_file[y,x]
        if brightness+50 >= 255:
            image_from_file[y,x] = 255
        else:
            image_from_file[y,x] = image_from_file[y,x] + 50

cv2.imshow('result', image_from_file)
cv2.waitKey()

