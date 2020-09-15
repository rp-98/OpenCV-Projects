import urllib.request
import cv2
import numpy as np
import time
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
URL = "https://192.168.1.100:8080/video"
video=cv2.VideoCapture(0)
video.open(URL)
while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    for x,y,w,h in face:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow('original',frame)
    if cv2.waitKey(1)==ord('q'):
        break
    print(type(face))
video.release()
cv2.destroyAllWindows()
