# -*- coding: utf-8 -*-

import cv2
import numpy as np

def detect(src):
    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(20,20))
    dst = src
    for (x, y, w, h) in face:
        cv2.rectangle(dst, (x, y), (x+w, y+h), (0,0,200), 3)
        
    return dst
        
def main():
    path = "img/face.jpg"
    img = cv2.imread(path)
    
    img = detect(img)
    
    cv2.imshow("output/detect_face.jpg", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()