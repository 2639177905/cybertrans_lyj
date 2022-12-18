# -*- coding: utf-8 -*-  
import cv2 as cv
import numpy as np
import os
def cv_filter2d(img_path):
    src = cv.imread(img_path)

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    dst = cv.filter2D(src, -1, kernel)
    return dst
    # cv.imshow('original', src)

    # cv.imshow('dst', dst)

    # cv.waitKey(0)
    # cv.destroyAllWindows()
enhancepath="./pictures/enhance"
ruihuapath="./pictures/ruihua"
filename=os.listdir(enhancepath)
for file in filename:
    p=enhancepath+"/"+file
    p2=ruihuapath+"/"+file
    print(p)
    img=cv_filter2d(p)
    
    cv.imwrite(p2,img)
