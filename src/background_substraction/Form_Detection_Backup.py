# importing libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
from skimage.measure import compare_ssim

scoring = {}
# original_ = cv2.imread('training/closing_barnängen.jpg', 0).astype(np.float32)
# original_ = cv2.imread('training/closing_botanicals.jpg', 0).astype(np.float32)
# original_ = cv2.imread('closing.jpg', 0).astype(np.float32)
# plt.figure()
# plt.imshow(original_)
# plt.show()


def check_match(template, original, file_name, frame):
    calculate_match(original, template, file_name, frame)
    pass


def calculate_match(original, template, file_name, frame):
    height = template.shape[1]
    width = template.shape[0]

    # img_match = cv2.matchTemplate(original, template, cv2.TM_CCORR_NORMED)
    # _, _, _, maxLoc = cv2.minMaxLoc(img_match)
    # rectangular = cv2.rectangle(original.copy(), (frame[0], frame[1]), (frame[2], frame[3]), 255, 3)
    match = original[frame[1] + 50:frame[1]+width + 50, frame[0]-45:frame[0]+height-45]
    plt.figure()
    plt.imshow(match, cmap='gray')
    plt.show()
    # img_match = cv2.matchTemplate(match, template, cv2.TM_CCORR_NORMED)
    # plt.figure()
    # plt.imshow(img_match, cmap='gray')
    # plt.show()
    score, diff = compare_ssim(template, match, full=True)
    file_name = file_name.replace(".jpg", "")
    file_name = file_name.replace("template_", "")
    scoring[file_name] = score
    print(file_name)
    print(score)

    # plt.show()
    # plt.subplot(121)
    # plt.imshow(img_match, cmap='gray')
    # plt.title('Matching'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122)
    # plt.imshow(rectangular, cmap='gray')
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.show()


def get_bottle(screenshot, frame):
    path = 'templates'

    files = []
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
                check_match(template_, screenshot, file, frame)
                files.append(os.path.join(r, file))

    print("Der Gewinner ist:")
    winner = max(scoring, key=scoring.get)
    print(str(winner).upper())
    return str(winner)


# template_ = cv2.imread('templates/template_barnängen.jpg', 0).astype(np.float32)
# plt.figure()
# plt.imshow(template_)
# plt.show()
# original_ = cv2.imread('training/closing_barnängen.jpg', 0).astype(np.float32)
# plt.figure()
# plt.imshow(original_)
# plt.show()

