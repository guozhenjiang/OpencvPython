import cv2
import numpy as np

img = cv2.imread('Resources/lambo.jpg')
print(img.shape)    # height width BGR

imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]    # height width

cv2.imshow("Image", img)
cv2.imshow("imgResize", imgResize)
cv2.imshow("imgCropped", imgCropped)

cv2.waitKey(0)