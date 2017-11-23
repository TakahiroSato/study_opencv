# -*- coding: utf-8 -*-

import cv2
import numpy as np
import detect_face
import binary_image
import detect_edge

def capture():
    cap = cv2.VideoCapture(0)
    cap.set(3, 800)
    cap.set(4, 600)
    
    while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame', detect_face.detect(frame))
        #cv2.imshow('gray', gray)
        #cv2.imshow('binary', binary_image.binarization(frame))
        '''
        cv2.imshow('edge', detect_edge.first_derivation(frame))
        cv2.imshow('prewitt', detect_edge.prewitt_filter(frame))
        cv2.imshow('sobel', detect_edge.sobel_filter(frame))
        cv2.imshow('laplacian', detect_edge.laplacian_filter(frame))
        cv2.imshow('emboss', detect_edge.emboss_filter(frame))
        '''
        cv2.imshow('canny', detect_edge.canny_filter(frame))
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    return cap

def main():
    capture().release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
    
