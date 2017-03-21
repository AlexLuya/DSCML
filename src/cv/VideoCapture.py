#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:05:59 2017

@author: alex
"""

import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    cv2.imshow('Captured',frame)
    cv2.imshow('Gray',gray)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()