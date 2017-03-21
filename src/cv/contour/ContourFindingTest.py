'''
Created on 17.03.2017

@author: alex
'''
import numpy as np
import cv2

im=cv2.imread('../../data/images/phone.png')
grayed=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
threshold=cv2.threshold(grayed,)
