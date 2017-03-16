#!/usr/local/bin/python2.7
# encoding: utf-8

import cv2

faceDetector=cv2.CascadeClassifier("../../data/opencv/haarcascades/haarcascade_frontalface_default.xml")
eyeDetector=cv2.CascadeClassifier("../../data/opencv/haarcascades/haarcascade_eye.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=faceDetector.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roiGray=gray[y:y+h,x:x+h]
        roiColor=img[y:y+h,x:x+h]
        eye=eyeDetector.detectMultiScale(roiGray)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roiColor,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
    cv2.imshow('img',img)
    k=cv2.waitKey(30)&0xff 
    if k==27:
        break
    
cap.release()
cv2.destroyAllWindows()          