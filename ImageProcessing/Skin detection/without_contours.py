import numpy as np
import argparse
import cv2

#lower and upper limits of skin colour
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")


image = cv2.imread('person3.jpg')

converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(converted, lower, upper)


output = cv2.bitwise_and(image, image, mask = mask)

#output = cv2.GaussianBlur(output, (3, 3), 0)    #optional- just so that the edges look smooth

cv2.imshow("images", np.hstack([image, output]))
cv2.waitKey(0)
