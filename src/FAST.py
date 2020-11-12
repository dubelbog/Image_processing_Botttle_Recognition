import numpy as np
import cv2
from matplotlib import pyplot as plt

img = plt.imread('resources/raw_images/conditioner.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector()

# find and draw the keypoints
kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(image=img, keypoints=kp, color=(255, 0, 0), outImage=open('resources/raw_images/test.jpg', 'rb'))

# Print all default params
print("Threshold: ", fast.getInt('threshold'))
print("nonmaxSuppression: ", fast.getBool('nonmaxSuppression'))
print("neighborhood: ", fast.getInt('type'))
print("Total Keypoints with nonmaxSuppression: ", len(kp))

cv2.imwrite('fast_true.png', img2)

# Disable nonmaxSuppression
fast.setBool('nonmaxSuppression', 0)
kp = fast.detect(img, None)

print("Total Keypoints without nonmaxSuppression: ", len(kp))

# img3 = cv2.drawKeypoints(img, kp, color=(255, 0, 0))
#
# cv2.imwrite('fast_false.png', img3)
