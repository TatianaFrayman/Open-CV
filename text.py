import numpy as np
import cv2 as cv
import cv2

image = np.zeros((480,640,3), dtype=np.uint8)
h,w = image.shape[:2]
cv2.line(image, (0,0), (640,480), (255, 100, 150), 3)
cv2.rectangle(image, (w//3, h//3), (w//3*2, h//3*2), (25,0,255), 1)
cv2.circle(image, (w//2, h//2), (h//3-3), (0,255,255), 3)

pts = np.array([[w//2, 0], [0,h], [w,h]], dtype= np.int32) #точки для построения треугольника
cv2.polylines(image, [pts], True, (255,255,0), 1) #треугольник по точкам
#cv2.fillPoly(image, [pts], (255,255,0), 1) #залитый треугольник

string = "What the fuck?!"
cv2.putText(image, string, (h//2-40, w//2-50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255,255,255))

cv2.imshow('IDraw', image)
cv2.waitKey()