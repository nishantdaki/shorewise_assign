#Image Processing
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read and Show Image in Window

img = cv2.imread("input.png", cv2.IMREAD_COLOR)
cv2.imshow("output", img)
cv2.waitKey(0)

# 2. Read Image in Grayscale and Show Image in Window / Save Image

img = cv2.imread("input.png", 0)
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

status = cv2.imwrite('output.jpg', img)  
print("Image written to file-system : ", status)  

# 3. Image Resizing

image = cv2.imread("input.png", cv2.IMREAD_COLOR)
half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
Titles =["Original", "Half"]
images =[image, half]
count = 2

for i in range(count):
	plt.subplot(2, 2, i + 1)
	plt.title(Titles[i])
	plt.imshow(images[i])

plt.show()

# 4. Rotate Image

img = cv2.imread("input.png", cv2.IMREAD_COLOR)

(h, w) = img.shape[:2]
center = (w / 2, h / 2)
angle90 = 90

M = cv2.getRotationMatrix2D(center, angle90, 1.0)
rotateimg = cv2.warpAffine(img, M, (w, h))

cv2.imshow("output", rotateimg)
cv2.waitKey(0)
cv2.destroyAllWindows()