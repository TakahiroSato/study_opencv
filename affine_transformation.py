# -*- coding: utf-8 -*-

import cv2
import numpy as np

def rotate_affine(src, theta, tx=0, ty=0):
    h, w = src.shape[0], src.shape[1]
    
    dst = np.zeros((h, w))
    
    rd = np.radians(theta)
        
    for y in range(0, h):
        for x in range(0, w):
            xi = (x-tx)*np.cos(rd) - (y-ty)*np.sin(rd) + tx
            yi = (x-tx)*np.sin(rd) + (y-ty)*np.cos(rd) + ty
            xi = int(xi)
            yi = int(yi)
            
            if yi < h-1 and xi < w-1 and yi > 0 and xi > 0:
                dst[y][x] = src[yi][xi]
                
    return dst
def main():
    path = "img/Lenna.bmp"
    gray = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)
    
    theta = 60
    
    oy, ox = int(gray.shape[0]/2), int(gray.shape[1]/2)
    
    dst = rotate_affine(gray, theta, ox, oy)
    
    cv2.imwrite("output/rotate_affine.bmp", dst)
    
    
if __name__ == "__main__":
    main()