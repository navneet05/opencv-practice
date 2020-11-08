# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:02:27 2020

@author: Navneet Yadav
"""
# %% 
import numpy as np
import cv2
# %% recording, saving video
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
fgbg = cv2.createBackgroundSubtractorMOG2() #detectShadows = False
#%%
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        fgmask = fgbg.apply(frame)
        img1_bg = cv2.bitwise_and(frame,frame,mask =fgmask)
        # Display the resulting frame
        cv2.imshow('frame', fgmask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
