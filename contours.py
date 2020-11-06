# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:28:47 2020

@author: Navneet Yadav
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
#%% image resize function
def resize(img,w):
    h_org, w_org = img.shape[:2]
    # Calculating the ratio 
    ratio = w / w_org
    # Creating a tuple containing width and height 
    dim = (w, int(h_org * ratio)) 
    # Resizing the image 
    return cv2.resize(img, dim)
#%%image preprocessing
img = cv2.imread('road.jpg')
img=resize(img, 700)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
edges = cv2.Canny(blurred,100,200)
imagepr(edges)
#%% finding contours change the source image
contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
imagepr(edges)
#%% drawing all contours
img1 = cv2.drawContours(img, contours, -1, (0,127,0), 3)
imagepr(img1)