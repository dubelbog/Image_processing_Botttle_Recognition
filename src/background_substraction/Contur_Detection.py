# importing libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
from skimage.measure import compare_ssim

scoring = {}
font = cv2.FONT_HERSHEY_COMPLEX
# original_ = cv2.imread('training/closing_barnängen.jpg', 0).astype(np.float32)
# original_ = cv2.imread('training/closing_botanicals.jpg', 0).astype(np.float32)
# original_ = cv2.imread('closing.jpg', 0).astype(np.float32)
# plt.figure()
# plt.imshow(original_)
# plt.show()


def check_match(template, original, file_name):
    calculate_match(original, template, file_name)
    pass


def calculate_match(original, template, file_name):
    height = template.shape[1]
    width = template.shape[0]

    img = cv2.imread("screenshot.jpg", cv2.IMREAD_GRAYSCALE)
    _, threshold = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("contours length: ")
    print(len(contours))
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        cv2.drawContours(img, [approx], 0, 0, 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if len(approx) > 25:
            cv2.putText(img, "Triangle", (x, y), font, 1, 0)
            print(len(approx))

    cv2.imshow("shapes", img)
    cv2.imshow("Threshold", threshold)

    # img_match = cv2.matchTemplate(original, template, cv2.TM_CCORR_NORMED)
    # _, _, _, maxLoc = cv2.minMaxLoc(img_match)
    # rectangular = cv2.rectangle(original.copy(), maxLoc, (maxLoc[0] + height, maxLoc[1] + width), 255, 3)
    # match = original[maxLoc[1]:maxLoc[1] + width, maxLoc[0]:maxLoc[0]+height]
    # plt.figure()
    # plt.imshow(match, cmap='gray')
    # plt.show()
    # score, diff = compare_ssim(template, match, full=True)
    # file_name = file_name.replace(".jpg", "")
    # file_name = file_name.replace("template_", "")
    # scoring[file_name] = score
    # print(file_name)
    # print(score)
    #
    # plt.show()
    # plt.subplot(121)
    # plt.imshow(img_match, cmap='gray')
    # plt.title('Matching'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122)
    # plt.imshow(rectangular, cmap='gray')
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.show()


def get_bottle(screenshot):
    path = 'templates'

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                file_path = os.path.join(r, file)
                template_ = cv2.imread(file_path, 0).astype(np.float32)
                plt.figure()
                plt.imshow(screenshot, cmap='gray')
                plt.savefig("screenshot.jpg")
                original = cv2.imread('screenshot.jpg', 0).astype(np.float32)
                check_match(template_, original, file)
                files.append(os.path.join(r, file))

    # print("Der Gewinner ist:")
    # winner = max(scoring, key=scoring.get)
    # print(str(winner).upper())


# template_ = cv2.imread('templates/template_barnängen.jpg', 0).astype(np.float32)
# plt.figure()
# plt.imshow(template_)
# plt.show()
# original_ = cv2.imread('training/closing_barnängen.jpg', 0).astype(np.float32)
# plt.figure()
# plt.imshow(original_)
# plt.show()
