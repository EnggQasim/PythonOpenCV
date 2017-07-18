import numpy as np
import matplotlib.pyplot as plt
import cv2

#								0
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_UNCHANGE = -1

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100],[80,100], 'c', linewidth='5')
plt.show()

cv2.imwrite('watchgray.png', img)
