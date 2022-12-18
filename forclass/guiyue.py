# -*- coding: utf-8 -*-  
import cv2 as cv
import numpy as np
import os
def jiangzao(img_path):
    src = cv.imread(img_path)
    for i in range(256):
        for j in range(256):
            for k in range(3):
                src[i,j,k]=round(src[i,j,k]/2)*2
    
    # cv.imshow('original', src)

    # cv.imshow('dst', dst)

    # cv.waitKey(0)
    # cv.destroyAllWindows()
    return src
jiangzaopath="./pictures/jiangzao"
guiyuepath="./pictures/guiyue"
filename=os.listdir(jiangzaopath)
for file in filename:
    p=jiangzaopath+"/"+file
    p2=guiyuepath+"/"+file
    print(p)
    img=jiangzao(p)
    
    cv.imwrite(p2,img)
