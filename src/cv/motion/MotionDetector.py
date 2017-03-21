import cv2 as cv
from datetime import datetime
import time
import numpy as np

class MotionDetectorInstantaneous():
    
    def onChange(self, val): #callback when the user change the detection threshold
        self.threshold = val
    
    def __init__(self,threshold=8, doRecord=True, showWindows=True):
        self.writer = None
        self.doRecord=doRecord #Either or not record the moving object
        self.show = showWindows #Either or not show the 2 windows
        self.frame = None
    
        self.capture=cv.VideoCapture(0)
        _,self.frame = self.capture.read() #Take a frame to init recorder
        if doRecord:
            self.initRecorder()
        
        self.frame1gray = np.zeros((self.frame.height, self.frame.width), dtype=cv.CV_8U) #Gray frame at t-1
        cv.cvtColor(self.frame, self.frame1gray, cv.COLOR_RGB2GRAY)
        
        #Will hold the thresholded result
        self.res = np.zeros((self.frame.height, self.frame.width), dtype=cv.CV_8U) #Gray frame at t-1
        
        self.frame2gray = np.zeros((self.frame.height, self.frame.width), dtype=cv.CV_8U) #Gray frame at t
        
        self.width = self.frame.width
        self.height = self.frame.height
        self.nb_pixels = self.width * self.height
        self.threshold = threshold
        self.isRecording = False
        self.trigger_time = 0 #Hold timestamp of the last detection
        
        if showWindows:
            cv.namedWindow("Image")
            cv.createTrackbar("Detection threshold: ", "Image", self.threshold, 100, self.onChange)
        
    def initRecorder(self): #Create the recorder
        codec = cv.VideoWriter_fourcc(*'MJPG') #('W', 'M', 'V', '2')
        self.writer=cv.VideoWriter(datetime.now().strftime("%b-%d_%H_%M_%S")+".wmv", codec, 5, self.frame.shape, 1)
        #FPS set to 5 because it seems to be the fps of my cam but should be ajusted to your needs

    def run(self):
        started = time.time()
        while True:
            
            _,curframe = self.capture.read()
            instant = time.time() #Get timestamp o the frame
            
            self.processImage(curframe) #Process the image
            
            if not self.isRecording:
                if self.somethingHasMoved():
                    self.trigger_time = instant #Update the trigger_time
                    if instant > started +5:#Wait 5 second after the webcam start for luminosity adjusting etc..
                        print datetime.now().strftime("%b %d, %H:%M:%S"), "Something is moving !"
                        if self.doRecord: #set isRecording=True only if we record a video
                            self.isRecording = True
            else:
                if instant >= self.trigger_time +10: #Record during 10 seconds
                    print datetime.now().strftime("%b %d, %H:%M:%S"), "Stop recording"
                    self.isRecording = False
                else:
                    cv.putText(curframe,datetime.now().strftime("%b %d, %H:%M:%S"), (25,30),cv.FONT_HERSHEY_SIMPLEX, 0) #Put date on the frame
                    self.writer.write(curframe) #Write the frame
            
            if self.show:
                cv.imshow("Image", curframe)
                cv.imshow("Res", self.res)
                
            self.frame1grayself.frame2gray.copy()
            c=cv.waitKey(1) % 0x100
            if c==27 or c == 10: #Break if user enters 'Esc'.
                break            
    
    def processImage(self, frame):
        cv.cvtColor(frame, self.frame2gray, cv.COLOR_RGB2GRAY)
        
        #Absdiff to get the difference between to the frames
        cv.absdiff(self.frame1gray, self.frame2gray, self.res)
        
        #Remove the noise and do the threshold
        cv.GaussianBlur(self.res, 5,5)
        cv.morphologyEx(self.res, cv.MORPH_OPEN)
        cv.morphologyEx(self.res, cv.MORPH_CLOSE)
        cv.threshold(self.res, 10, 255, cv.THRESH_BINARY_INV)

    def somethingHasMoved(self):
        nb=0 #Will hold the number of black pixels

        for x in range(self.height): #Iterate the hole image
            for y in range(self.width):
                if self.res[x,y] == 0.0: #If the pixel is black keep it
                    nb += 1
        avg = (nb*100.0)/self.nb_pixels #Calculate the average of black pixel in the image

        if avg > self.threshold:#If over the ceiling trigger the alarm
            return True
        else:
            return False
        
if __name__=="__main__":
    detect = MotionDetectorInstantaneous(doRecord=True)
    detect.run()
