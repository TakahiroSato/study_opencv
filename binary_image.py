# -*- coding: utf-8 -*-

import cv2
import numpy as np

def binarization(src, threshold=127):
    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    th1 = gray.copy()
    
    th1[gray < threshold] = 0
    th1[gray >= threshold] = 255
    
    return th1

def main():
    path = "img/Lenna.bmp"
    t = 100
    img = cv2.imread(path)
    
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    th1 = gray.copy()
    
    th1[gray < t] = 0
    th1[gray >= t] = 255
    
    cv2.imwrite("output/output.bmp", th1)
    

if __name__ == "__main__":
    main()

