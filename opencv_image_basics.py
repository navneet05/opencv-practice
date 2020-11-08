# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:30:23 2020

@author: hp
"""
import cv2
import numpy as np

#checking opencv version
print(cv2.__version__)
#%% function to view image
def imagepr(img):
    cv2.imshow('image', img) 
    k = cv2.waitKey(0) & 0xFF
  
    # wait for ESC key to exit 
    if k == 27:  
        cv2.destroyAllWindows() 
      
    # wait for 's' key to save and exit 
    elif k == ord('s'):  
        cv2.imwrite('copy.png',img) 
        cv2.destroyAllWindows() 
#%% Reading the image using imread() function 
image = cv2.imread('road.jpg') #1(default) for normal image, 0 for grayscale, -1 for unchanged
imagepr(image)
#%% image shape,size,datatype,resize,slicing

# Extracting the height and width of an image 
h, w = image.shape[:2] 
print(image.shape)

# Displaying the height and width 
print("Height = {},  Width = {}".format(h, w)) 

#image size and data type
print("{} {}".format(image.size,image.dtype))

#resizing the image while maintaing aspect ratio 
# Calculating the ratio 
ratio = 800 / w 
# Creating a tuple containing width and height 
dim = (800, int(h * ratio)) 
# Resizing the image 
resize_aspect = cv2.resize(image, dim) 

# slicing the pixels of the image for Region of Image
roi = image[100 : 500, 200 : 700] 
imagepr(roi)
#%%Splitting and Merging Image Channels "BGR"
b,g,r = cv2.split(image)
img = cv2.merge((b,g,r))

#%% changing colour-space
img_gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #for hsv cv2.COLOR_BGR2HSV
imagepr(img_gray)
