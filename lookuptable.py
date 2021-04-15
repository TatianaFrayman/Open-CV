import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("C:/Users/asus/Desktop/gray_woman.jpg")
print(image.shape)
gamma = 0.1
table = np.zeros((256), dtype=np.uint8)
for i in range(256):
    table[i] = round((i/255)**gamma*255)

image_res = cv2.LUT(image, table)
cv2.imshow('result', np.hstack((image, image_res)))
cv2.waitKey()
cv2.destroyAllWindows()