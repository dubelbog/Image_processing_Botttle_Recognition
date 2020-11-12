# importing libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt
from Form_Detection import get_bottle


font = cv2.FONT_HERSHEY_COMPLEX
text = 'To recognize the shape of the bottle, put it in the white frame'
frame = [200, 80, 530, 680]


def get_image_shape(fgmask2):
    plt.figure()
    plt.imshow(fgmask2)
    plt.savefig("test.jpg")
    kernel = np.ones((7, 7), np.uint8)
    # img1 = cv2.imread("test.jpg", 2)
    closing = cv2.morphologyEx(fgmask2, cv2.MORPH_CLOSE, kernel)
    # contours, _ = cv2.findContours(fgmask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # ret, bw_img = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
    plt.figure()
    plt.imshow(closing)
    plt.savefig("closing.jpg")
    print("Es handelt sich um die Shampoo Flasche BOTANICALS")


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("nothing")
    if event == cv2.EVENT_RBUTTONDOWN:
        red = img[y, x, 2]
        blue = img[y, x, 0]
        green = img[y, x, 1]
        print(red, green, blue)
        strRGB = str(red) + "," + str(green) + "," + str(blue)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, strRGB, (x, y), font, 1, (240, 155, 55), 2)
        cv2.imshow('original', img)


# creating object
fgbg = cv2.createBackgroundSubtractorMOG2()

# capture frames from a camera
cap = cv2.VideoCapture(0)

while True:
    # read frames
    ret, img = cap.read()
    # apply mask for background subtraction
    fgmask = fgbg.apply(img)

    cv2.imshow('Original', img)
    cv2.putText(fgmask,
                text,
                (25, 25),
                font, 0.5,
                (255, 255, 255),
                1,
                cv2.LINE_4)
    # set white frame
    rectangular = cv2.rectangle(fgmask, (frame[0], frame[1]), (frame[2], frame[3]), 255, 1)
    cv2.imshow('MOG2', fgmask)
    cv2.setMouseCallback("Original", click_event)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if k == ord('t'):
        kernel = np.ones((50, 50), np.uint8)
        screenshot = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
        plt.imshow(fgmask, cmap='gray')
        plt.savefig("screenshot.jpg")
        original = cv2.imread('screenshot.jpg', 0).astype(np.float32)
        text = get_bottle(original, frame)
        text = str(text).upper()
        continue

cap.release()
cv2.destroyAllWindows()
