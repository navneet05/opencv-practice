# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:03:41 2020

@author: Navneet Yadav
"""
import cv2 
import numpy as np 
#%% function to view image
def imagepr(img):
    cv2.imshow('image', img) 
    k = cv2.waitKey(0) & 0xFF
  
    # wait for ESC key to exit 
    if k == 27:  
        cv2.destroyAllWindows() 
      
    # wait for 's' key to save and exit 
    elif k == ord('s'):  
        cv2.imwrite('match.png',img) 
        cv2.destroyAllWindows() 
#%% Read the images 
img = cv2.imread('pm_main.jpg')
template = cv2.imread('pm_template.jpg',0)
#%%
# Convert img to grayscale 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# Store width and height of template in w and h 
h, w = template.shape[:2]  
#%%
# Perform match operations. 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 

#%% Specify a threshold 
threshold = 0.8
# Store the coordinates of matched area in a numpy array 
loc = np.where( res >= threshold) 

#%% Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
	cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2) 

# Show the final image with the matched area. 
imagepr(img) 
