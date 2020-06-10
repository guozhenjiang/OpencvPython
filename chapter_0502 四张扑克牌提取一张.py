import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height = 250, 350

pts1 = np.float32([[412,260], [14,339], [519,786], [124,865]])
pts2 = np.float32([[0, height], [width, height], [0, 0], [width, 0]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOut)

cv2.waitKey(0)