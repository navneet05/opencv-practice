# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:48:53 2020

@author: Navneet Yadav
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('road.jpg')
#%% ploting 1-dimensional histrogram
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.hist(gray.ravel(),256,[0,256])
plt.show()
#%% ploting 2-dimensional histrogram for hsv image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
plt.imshow(hist,interpolation = 'nearest')
plt.show()