import cv2
import numpy as np

img = cv2.imread("Resources/lambo.jpg")

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Orignal", img)
cv2.imshow("HSV", imgHSV)

cv2.waitKey(0)