import sys

# import the necessary things for OpenCV
from opencv import cv
from opencv import highgui
from opencv.cv import *
from opencv.highgui import *

import pygame
from pygame.locals import *
import Numeric
import random

Fs=44100 # sample rate
pygame.mixer.init(Fs, -16,1)   # mono, 16-bit

def drawRectangle(faces, image):
    if faces:
        for face in faces:
            cvRectangle(image, cvPoint( int(face.x), int(face.y)), cvPoint(int(face.x+face.width)-30, int(face.y+face.height)-30), CV_RGB(0,255,0), 3, 8, 0)
            note(int(face.x/10)*6.0+200, 20.0)
#            print face.x + face.y + face.width + face.height

def detectFace(image):
    grayscale = cvCreateImage(cvSize(640, 480), 8, 1)
    cvCvtColor(image, grayscale, CV_BGR2GRAY)
    storage = cvCreateMemStorage(0)
    cvClearMemStorage(storage)
    cvEqualizeHist(grayscale, grayscale)
    cascade = cvLoadHaarClassifierCascade('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml', cvSize(1,1))
    faces = cvHaarDetectObjects(grayscale, cascade, storage, 1.1, 2, CV_HAAR_DO_CANNY_PRUNING, cvSize(100,100))
    drawRectangle(faces, image)

def note(freq, amp):
    length = Fs * 0.2
    tmp = []
    for t in range(int(length)):
            v= amp * Numeric.sin(t*freq/Fs*2*Numeric.pi)
            tmp.append(v)
    pygame.sndarray.make_sound(Numeric.array(tmp,Numeric.Int0)).play()

def main():

    print "FaceIn! an OpenCV Python Face Recognition Program"
    highgui.cvNamedWindow ('Camera', highgui.CV_WINDOW_AUTOSIZE)
    highgui.cvMoveWindow ('Camera', 10, 10)
    device = -1
    capture = highgui.cvCreateCameraCapture (device)
    frame = highgui.cvQueryFrame (capture)
    frame_size = cv.cvGetSize (frame)
    fps = 30
        
    while 1:
        
        frame = highgui.cvQueryFrame (capture)
        
        detectFace(frame)
        # display the frames to have a visual output
        highgui.cvShowImage ('Camera', frame)

        # handle events
        k = highgui.cvWaitKey (5)

        if k % 0x100 == 27:
            # user has press the ESC key, so exit
            quit()
        
if __name__ == "__main__":
  main()