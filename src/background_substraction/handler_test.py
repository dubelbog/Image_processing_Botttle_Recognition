from skimage.measure import compare_ssim
import numpy as np
import cv2

template = cv2.imread('training/closing_barnängen.jpg', 0).astype(np.float32)
match = template
score, diff = compare_ssim(template, match, full=True)
print(score)

