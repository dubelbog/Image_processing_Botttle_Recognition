import numpy as np
import cv2
from matplotlib import pyplot as plt

img = plt.imread('resources/raw_images/conditioner.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(gray, cmap='gray')
plt.show()

output = img

corners = cv2.goodFeaturesToTrack(gray, 1000, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(output, (x, y), 20, 0, -1)

plt.figure()
plt.imshow(output)
plt.savefig("output.jpg")
plt.show()
