# -*- coding: utf-8 -*-

import cv2
import numpy as np

def filter2d(src, kernel):
    m, n = kernel.shape
    
    d = int((m-1)/2)
    h, w = src.shape[0], src.shape[1]
    
    dst = np.zeros((h, w))
    
    for y in range(d, h-d):
        for x in range(d, w-d):
            dst[y][x] = np.sum(src[y-d:y+d+1, x-d:x+d+1]*kernel)
            
            
    return dst

def  first_derivation(src):
    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    
    kernel = np.array([[0,0,0],
                       [-1,0,1],
                       [0,0,0]])
    
    #return filter2d(gray, kernel)
    return cv2.filter2D(gray, cv2.CV_64F, kernel)


def prewitt_filter(src):
    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    
    kernel = np.array([[-1,0,1],
                       [-1,0,1],
                       [-1,0,1]])
    
    return cv2.filter2D(gray, cv2.CV_64F, kernel)