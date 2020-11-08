# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:01:39 2020

@author: Navneet Yadav
"""
#%%
import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#%% face detect in image
img = cv2.imread('profile_online.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%% face detect in VideoCapture
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()