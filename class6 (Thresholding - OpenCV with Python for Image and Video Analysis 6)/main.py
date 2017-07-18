import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2. cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)

cv2.imshow('Original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('theshold2', threshold2)
cv2.imshow('Gaussian', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()