# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:51:39 2020

@author: Navneet Yadav
"""
import cv2
import numpy as np
#%% function to resize image
#resizing the image while maintaing aspect ratio 
def resize(img,w):
    h_org, w_org = img.shape[:2]
    # Calculating the ratio 
    ratio = w / w_org
    # Creating a tuple containing width and height 
    dim = (w, int(h_org * ratio)) 
    # Resizing the image 
    return cv2.resize(img, dim)
#%%
def canny(img):    
    mean=np.median(img) #try mean and meadian both use one which is better
    min_threshold = 0.66 * mean
    max_threshold = 1.33 * mean
    edge=cv2.Canny(img,min_threshold,max_threshold)
    return edge
#%%
img = cv2.imread('road.jpg',0)
img=resize(img, 400)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(blurred,100,300) #recomended ratio-1:2,1:3
edge=canny(blurred)
#%%
while(1):
    stacked = np.hstack((img,edges,edge))
    # Show this stacked frame at whatever % of the size.
    cv2.imshow("show",cv2.resize(stacked,None,fx=1,fy=1))
    k = cv2.waitKey(5) & 0xFF
    # wait for ESC key to exit 
    if k == 27:  
        cv2.destroyAllWindows() 
        break
    # wait for 's' key to save and exit 
    elif k == ord('s'):  
        cv2.imwrite('stacked.png',stacked) 
        cv2.destroyAllWindows()
        break