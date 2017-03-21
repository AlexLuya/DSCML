'''
Created on 21.03.2017

@author: alex
'''
import cv2
import numpy as np

image = cv2.imread("../../data/images/hand_01.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]

h1, w1 = gray.shape[:2]
h2, w2 = thresh.shape[:2]

#create empty matrix
vis = np.zeros((max(h1, h2), w1+w2), np.uint8)

#combine 2 images
vis[:h1, :w1] = thresh
vis[:h2, w1:w1+w2] = gray
# # show the output image
cv2.imshow("Image", vis)
cv2.waitKey(0)