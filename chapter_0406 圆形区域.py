import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img)
# img[:] = 255, 0, 0  # BGR

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 3)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), cv2.FILLED)
cv2.circle(img, (400, 50), 50, (255, 255, 0), 5)
cv2.circle(img, (400, 50), 30, (0, 255, 0), cv2.FILLED)

cv2.imshow("Image", img)

cv2.waitKey(0)