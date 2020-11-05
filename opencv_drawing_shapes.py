# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:14:36 2020

@author: hp
"""
import cv2
import numpy as np

#%% function to view image
def imagepr(img):
    cv2.imshow('image', img) 
    k = cv2.waitKey(0) & 0xFF
  
    # # wait for 's' key to save and exit
    if k == ord('s'):  
        cv2.imwrite('copy.png',img) 
        cv2.destroyAllWindows()  
    # any key to exit 
    else :
        cv2.destroyAllWindows() 
#%%
# Create a black image
img = np.zeros((512,512,3), np.uint8)
#%%
imagepr(img)
#%% draw line-you need to pass starting and ending coordinates of line
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)
#%% draw a rectangle-top-left corner and bottom-right corner of rectangle
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#%% draw a circle-need its center coordinates and radius
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
#%% inserting text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
