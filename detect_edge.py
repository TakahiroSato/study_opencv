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