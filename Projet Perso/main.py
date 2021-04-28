import cv2 as cv
import numpy as np

width = 640
height = 480

cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of color in HSV
    color = np.uint8([[frame[int(height/2)][int(width/2)]]])
    hsv_color = cv.cvtColor(color,cv.COLOR_BGR2HSV)
    print(hsv_color[0][0][0])
    lower_color = np.array([hsv_color[0][0][0]-5,50,50])
    upper_color = np.array([hsv_color[0][0][0]+5,255,255])
    # Threshold the HSV image to get only color colors
    mask = cv.inRange(hsv, lower_color, upper_color)
    # Close and open image
    kernel = np.ones((6,6),np.uint8)
    binclose = cv.erode(mask, kernel)
    binopen = cv.dilate(binclose, kernel)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= binopen)

    cv.line(frame, (int(width/2), int(height/2) - 10), (int(width/2), int(height/2) + 10), (255,255,255), 2)
    cv.line(frame, (int(width/2) - 10, int(height/2)), (int(width/2) + 10, int(height/2)), (255,255,255), 2)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    cv.imshow('binclose',binclose)
    cv.imshow('binopen',binopen)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()


