import cv2
import numpy as np

img = cv2.imread('hand.jpg')

lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")

converted = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(converted, lower, upper)

ret, thresh = cv2.threshold(mask , 250, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
