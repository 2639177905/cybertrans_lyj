from PIL import Image
from PIL import ImageEnhance
import os

rawpath="./pictures/raw"
enhancepath="./pictures/enhance"
filename=os.listdir(rawpath)
print(filename)
for file in filename:
    p=rawpath+"/"+file
    p1=enhancepath+"/"+file
    img = Image.open(p)
    # img.show()

    #对比度增强  
    enh_con = ImageEnhance.Contrast(img)  
    contrast = 1.5  
    img_contrasted = enh_con.enhance(contrast)  
    # img_contrasted.show() 
    img_contrasted.save(p1)