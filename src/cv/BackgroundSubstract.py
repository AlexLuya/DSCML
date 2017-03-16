# -*- coding: utf-8 -*-

import cv2

cap = cv2.VideoCapture('../../data/opencv/vtest.avi')
#cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorKNN()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
