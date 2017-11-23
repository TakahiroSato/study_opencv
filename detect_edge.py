# -*- coding: utf-8 -*-

import cv2
import numpy as np

ddepth = -1 #cv2.CV_64F

def filter2d(src, kernel, ddepth=-1):
    return cv2.filter2D(__cvt_gray(src), ddepth, kernel)
    
    '''
    m, n = kernel.shape
    
    d = int((m-1)/2)
    h, w = src.shape[0], src.shape[1]
    
    dst = np.zeros((h, w))
    
    for y in range(d, h-d):
        for x in range(d, w-d):
            dst[y][x] = np.sum(src[y-d:y+d+1, x-d:x+d+1]*kernel)
            
    return dst
    '''

def __cvt_gray(src):
    return cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

def  first_derivation(src):
    kernel = np.array([[0, 0, 0],
                       [-1,0, 1],
                       [0, 0, 0]])
    
    return cv2.filter2D(__cvt_gray(src), ddepth, kernel)

def prewitt_filter(src):
    kernel = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]])
    
    return cv2.filter2D(__cvt_gray(src), ddepth, kernel)

def sobel_filter(src):
    kernel = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]])
    
    return cv2.filter2D(__cvt_gray(src), ddepth, kernel)

def laplacian_filter(src):
    kernel = np.array([[1, 1, 1],
                       [1,-8, 1],
                       [1, 1, 1]])
    
    return cv2.filter2D(__cvt_gray(src), ddepth, kernel)

def emboss_filter(src):
    kernel = np.array([[-2,-1, 0],
                       [-1, 1, 1],
                       [-1, 1, 2]])
    
    offset = 128
    return cv2.filter2D(__cvt_gray(src), ddepth, kernel, delta=offset)

def canny_filter(src, low_thresh=100, high_thresh=200):
    return cv2.Canny(__cvt_gray(src), low_thresh, high_thresh)






