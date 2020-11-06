# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:03:13 2020

@author: Navneet Yadav
"""
import cv2
import numpy as np
temp=0
#%% function to view image
def imagepr(img,temp):
    cv2.imshow('image', img) 
    k = cv2.waitKey(0) & 0xFF
  
    # # wait for 's' key to save and exit
    if k == ord('s'):
        name="temp"+str(temp)+".png"
        cv2.imwrite(name,img) 
        cv2.destroyAllWindows()
        return temp+1
    # any key to exit 
    else :
        cv2.destroyAllWindows() 
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
#%% Load two images
img1 = cv2.imread('road.jpg')
img2 = cv2.imread('opencv_logo.png')
img1=resize(img1, 1000)
img2=resize(img2, 400)
imagepr(img1,temp)
imagepr(img2,temp)
#%% I want to put logo on top-left corner, So I create a ROI
rows,cols = img2.shape[:2]
roi = img1[0:rows, 0:cols ]
imagepr(roi,temp)
#%% Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
temp=imagepr(mask,temp)
temp=imagepr(mask_inv,temp)
#%% Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
imagepr(img1_bg, temp)
#%% Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
imagepr(img2_fg, temp)
#%% Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
imagepr(img1, temp)