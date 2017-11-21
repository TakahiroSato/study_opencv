# -*- coding: utf-8 -*-

import cv2
import numpy as np

def resize_nearest(src, h, w):
    dst = np.empty((h, w))
    hi, wi = src.shape[0], src.shape[1]
    
    ax = w / float(wi)
    ay = h / float(hi)
    
    for y in range(0, h):
        for x in range(0, w):
            xi, yi = int(round(x/ax)), int(round(y/ay))
            if xi > wi -1: xi = wi -1
            if yi > hi -1: yi = hi -1
            
            dst[y][x] = src[yi][xi]
            
    return dst

def resize_bilinear(src, h, w):
    dst = np.empty((h, w))
    hi, wi = src.shape[0], src.shape[1]
    
    ax = w / float(wi)
    ay = h / float(hi)
    
    for y in range(0, h):
        for x in range(0, w):
            xi, yi = x/ax, y/ay
            x0, y0 = int(xi), int(yi)
            if x0 > wi -2: x0 = wi -2
            if y0 > hi -2: y0 = hi -2
            
            dx = xi - x0
            dy = yi - y0
            
            dst[y][x] = (1-dx)*(1-dy)*src[y0][x0] + \
                        dx*(1-dy)*src[y0][x0+1] + \
                        (1-dx)*dy*src[y0+1][x0] + \
                        dx*dy*src[y0+1][x0+1]
                        
    return dst
                        

def main_resize_nearest():
    path = "img/Lenna.bmp"
    img = cv2.imread(path)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    dst1 = resize_nearest(gray, gray.shape[1]*4, gray.shape[0]*4)
    
    cv2.imwrite("output/resize.bmp", dst1)
    
def main_resize_bilinear():
    path = "img/Lenna.bmp"
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dst1 = resize_bilinear(gray, gray.shape[1]*4, gray.shape[0]*4)
    cv2.imwrite("output/resize_bilinear.bmp", dst1)
    
def main():
    main_resize_bilinear()

if __name__ == "__main__":
    main()