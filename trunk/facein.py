# TODO FIRST:

# Detect face
# Extract face
# Average the image
# Compare with the images in the database


# TODO SECOND:

# Segment the extracted face by 10px x 10px
# Get average of every segment and store the values
# Compare these values with every averaged face in the database
# Print the closest found one.

import sys
# import the necessary things for OpenCV
from opencv import cv
from opencv import highgui
from opencv.cv import *
from opencv.highgui import *



def detectFace(image):

    grayscale = cvCreateImage(cvSize(640, 480), 8, 1)
    cvCvtColor(image, grayscale, CV_BGR2GRAY)
    storage = cvCreateMemStorage(0)
    cvClearMemStorage(storage)
    cvEqualizeHist(grayscale, grayscale)
    cascade = cvLoadHaarClassifierCascade('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml', cvSize(1,1))
    faces = cvHaarDetectObjects(grayscale, cascade, storage, 1.1, 2, CV_HAAR_DO_CANNY_PRUNING, cvSize(100,100))
    drawRectangle(faces, image)



def drawRectangle(faces, image):

    if faces:
        for face in faces:
            cvRectangle(image, cvPoint( int(face.x), int(face.y)), cvPoint(int(face.x+face.width)-30, int(face.y+face.height)-30), CV_RGB(0,255,0), 3, 8, 0)



def main():

    print "FaceIn! an OpenCV Python Face Recognition Program"
    
    highgui.cvNamedWindow ('Camera', highgui.CV_WINDOW_AUTOSIZE)
    highgui.cvMoveWindow ('Camera', 10, 10)
    device = 0 #use first device found
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