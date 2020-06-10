import cv2
import numpy as np

img = cv2.imread('Resources/lambo.jpg')
print(img.shape)    # height width BGR

cv2.imshow("Image", img)

cv2.waitKey(0)