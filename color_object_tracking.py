# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:00:39 2020

@author: Navneet Yadav
"""
import cv2
import numpy as np
#%% function for lower and upper value of color
def lowup():
   color = np.uint8([[[9,9,234 ]]])
   hsv_value = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
   a,b,c=cv2.split(hsv_value)
   del b,c
   h=int(a)
   return np.array([h-10,100,100]), np.array([h+10,255,255])
lowup()
#%% MAIN CODE
cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_value,upper_value=lowup() #np.array([110,50,50]),np.array([130,255,255])

    # Threshold the HSV image to get only blue colors-binary image
    mask = cv2.inRange(hsv, lower_value, upper_value)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    # Converting the binary mask to 3 channel image, this is just so we can stack it
    mask_1= cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    # stack the mask, orginal frame and the filtered result
    stacked = np.hstack((frame,mask_1,res))
    
    # Show this stacked frame at 40% of the size.
    cv2.imshow("show",cv2.resize(stacked,None,fx=0.7,fy=1))
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()