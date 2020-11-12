# importing libraries
import numpy as np
import cv2
import time
from matplotlib import pyplot as plt
from Form_Detection import get_bottle


font = cv2.FONT_HERSHEY_COMPLEX
text = 'To recognize the shape of the bottle, put it in the white frame'
text_img = 'Welcome to bottle shape recognition app!'
frame = [200, 80, 530, 680]

# creating object
fgbg = cv2.createBackgroundSubtractorMOG2()

# capture frames from a camera
cap = cv2.VideoCapture(0)

while True:
    # read frames
    ret, img = cap.read()
    # apply mask for background subtraction
    fgmask = fgbg.apply(img)
    cv2.putText(img,
                text_img,
                (25, 25),
                font, 0.5,
                (0, 0, 0),
                2,
                cv2.LINE_4)

    cv2.imshow('Original', img)
    cv2.putText(fgmask,
                text,
                (25, 25),
                font, 0.5,
                (255, 255, 255),
                1,
                cv2.LINE_4)
    rectangular = cv2.rectangle(fgmask, (frame[0], frame[1]), (frame[2], frame[3]), 255, 1)
    cv2.imshow('MOG2', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if k == ord('t'):
        kernel = np.ones((100, 100), np.uint8)
        screenshot = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
        plt.imshow(fgmask, cmap='gray')
        plt.savefig("screenshot.jpg")
        original = cv2.imread('screenshot.jpg', 0).astype(np.float32)
        text = get_bottle(original)
        text = str(text).upper()
        text_img = text
        continue

cap.release()
cv2.destroyAllWindows()
