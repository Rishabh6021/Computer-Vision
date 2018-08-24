import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')  #Loads a face classifier from xml file
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')                   #Loads a eye classifier from xml file

img = cv.imread('a7.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                                  #Converts the image from RGB to gray format

faces = face_cascade.detectMultiScale(gray, 1.3, 4)                         #Detects objects of different sizes in the input image.They are returned as a list of rectangles.

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)                           #Draws bounding rectangle around faces detected in the image

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex,ey,ew,eh) in eyes:                                              #Draws bounding rectangle around eyes detected in the image
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()