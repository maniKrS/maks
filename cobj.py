import cv2
import time
import numpy as np

video = cv2.VideoCapture(0)
tracker = cv2.TrackerCSRT_create()

while True:
    success,img = video.read()
    cv2.imshow("frame",img)
    key = cv2.waitKey(1)
    if key == 32:
        break
cv2.destroyAllWindows()