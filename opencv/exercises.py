# -*- coding: utf-8 -*-
import cv2
import numpy
import os,os.path
import datetime

def ByteToImage():
    # Make an array of 120,000 random bytes.
    randomByteArray = bytearray(os.urandom(120000))
    flatNumpyArray = numpy.array(randomByteArray)
    # Convert the array to make a 400x300 grayscale image.
    grayImage = flatNumpyArray.reshape(300, 400)
    cv2.imwrite('RandomGray.png', grayImage)
    # Convert the array to make a 400x100 color image.
    bgrImage = flatNumpyArray.reshape(100, 400, 3)
    cv2.imwrite('RandomColor.png', bgrImage)

def VideoCaptureAndWriter():
    videoCapture = cv2.VideoCapture('F:/UndergraduateThesis/opencv/PracticeMaterials/WhatWomenWant.AVI')
    fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
    int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
    videoWriter = cv2.VideoWriter(
    'MyOutputVid.avi', cv2.cv.CV_FOURCC('I','4','2','0'), fps, size)
    success, frame = videoCapture.read()
    while success: # Loop until there are no more frames.
        videoWriter.write(frame)
        success, frame = videoCapture.read()

def VideoCaptureAndSavePic():
    directoryPath = 'F:/UndergraduateThesis/opencv/PracticeMaterials/video/'
    capturePicDir = 'F:/UndergraduateThesis/opencv/PracticeMaterials/capture/'
    for file in os.listdir(directoryPath):
        videoCapture = cv2.VideoCapture(directoryPath+file)
        if not videoCapture:
            return None
        fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
        PERIOD = fps*60*3 # Capture video per 10s
        size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
        print(PERIOD)
        print(int(PERIOD))
        fileName = os.path.splitext(file)[0]
        subDirectory = capturePicDir+fileName
        if not os.path.exists(subDirectory):
            os.makedirs(subDirectory)
        count = 1
        while True:
            print('#'+str(count)+'starting capturing...')
            success, frame = videoCapture.read()
            for i in range(1,int(PERIOD)):
                success, frame = videoCapture.read()
                if not success:
                    return None

            cv2.imwrite(subDirectory+'/'+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg',frame)
            count += 1
            if count == 3:
                break;

def test():
    directoryPath = 'F:/UndergraduateThesis/opencv/PracticeMaterials/'
    for files in os.listdir(directoryPath):
        print files
        print os.path.abspath(files)
        print os.path.basename(files)
        print os.path.splitext(files)
        print os.path.splitext(files)[0]
        print datetime.datetime.now().strftime('%Y%m%d%H%M%S')





if __name__=='__main__':
    VideoCaptureAndSavePic()
    #test()
