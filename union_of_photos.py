import numpy as np
import cv2 as cv
import cv2

putine = cv2.imread('C:/Users/asus/Desktop/rgb.png')
(h, w) = putine.shape[:2]
one_ph = np.zeros([h//3,w], dtype = np.uint8)

b = putine[0:h//3, :]
g = putine[h//3: 2*h//3, :]
r = putine[2*h//3:h, :]

one_ph = b+g+r

cv2.imshow('union', one_ph)
cv2.waitKey()
cv2.destroyAllWindows()