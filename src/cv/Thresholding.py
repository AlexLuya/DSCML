'''
Created on 28.02.2017

@author: alex
'''
import cv2

img = cv2.imread('../../data/opencv/bookpage.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('original',img)
cv2.imshow('threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()