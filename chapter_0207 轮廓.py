import cv2

img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny_100_100 = cv2.Canny(img, 100, 100)
imgCanny_150_200 = cv2.Canny(img, 150, 200)

cv2.imshow('Raw Image', img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image 1', imgCanny_100_100)
cv2.imshow('Canny Image 2', imgCanny_150_200)
cv2.waitKey(0)