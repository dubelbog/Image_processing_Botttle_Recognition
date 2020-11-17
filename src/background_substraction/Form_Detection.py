# importing libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
from skimage.measure import compare_ssim

scoring = {}


def calculate_match(template, original, file_name):
    height = template.shape[1]
    width = template.shape[0]
    img_match = cv2.matchTemplate(original, template, cv2.TM_CCORR_NORMED)
    _, _, _, maxLoc = cv2.minMaxLoc(img_match)
    img_match = original[maxLoc[1]:maxLoc[1]+width, maxLoc[0]:maxLoc[0]+height]
    plt.figure()
    plt.imshow(img_match, cmap='gray')
    plt.show()
    score, diff = compare_ssim(img_match, template, full=True)
    file_name = file_name.replace(".jpg", "")
    file_name = file_name.replace("template_", "")
    scoring[file_name] = score
    print(file_name)
    print(score)


def get_bottle(screenshot):
    path = 'templates'
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                file_path = os.path.join(r, file)
                template_ = cv2.imread(file_path, 0).astype(np.float32)
                plt.figure()
                plt.imshow(template_, cmap='gray')
                plt.show()
                plt.figure()
                calculate_match(template_, screenshot, file)
    sorted_list = sorted(scoring.values(), reverse=True)
    if sorted_list[0] < 0.15 or sorted_list[0] - sorted_list[1] < 0.05:
        text = "It was not possible to calculate the shape recognition. Try one more time."
    else:
        text = str(max(scoring, key=scoring.get)).upper()
    return text

