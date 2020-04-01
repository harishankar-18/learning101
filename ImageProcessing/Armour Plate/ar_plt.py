import cv2
import numpy as np

img = cv2.imread('robot.jpg')



lower = np.array([20,10,210], dtype = "uint8")
upper = np.array([50,120,255], dtype = "uint8")

converted = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(converted, lower, upper)

output = cv2.bitwise_and(img, img, mask = mask)

ret, thresh = cv2.threshold(mask , 250, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)


cv2.imshow("images", np.hstack([img, output]))
cv2.waitKey(0)

#found contours of the red LEDs. Don't know how to procceed after this
#maybe I can find the corners of the contour and draw a polygon with those points but I can't get rid of the left led and the 4 in the image
