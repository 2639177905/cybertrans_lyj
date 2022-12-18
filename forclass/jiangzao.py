# -*- coding: utf-8 -*-  
import cv2 as cv
import numpy as np
import os
def jiangzao(img_path):
    src = cv.imread(img_path)
    
    denoise_2 = cv.fastNlMeansDenoisingColored(src,None,5,5,7,21)
    return denoise_2
    # cv.imshow('original', src)

    # cv.imshow('dst', dst)

    # cv.waitKey(0)
    # cv.destroyAllWindows()
ruihuapath="./pictures/ruihua"
jiangzaopath="./pictures/jiangzao"
filename=os.listdir(ruihuapath)
for file in filename:
    p=ruihuapath+"/"+file
    p2=jiangzaopath+"/"+file
    print(p)
    img=jiangzao(p)
    
    cv.imwrite(p2,img)
