'''
Created on 18.03.2017

@author: alex
'''
# import the necessary packages
import cv2

books=cv2.imread("../../../data/images/books.jpg")
grayed=cv2.cvtColor(books,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayed books",grayed)
gaussioned=cv2.GaussianBlur(grayed,(3,3),0)
# cv2.imshow("Original books",books)
cv2.imshow("Gaussianed books",gaussioned)

cv2.waitKey(0)