#!/usr/bin/env python
import os
from PIL import Image

#遍历目录读取所有图片
def searchImage(path):
    pics = []
    for p in os.listdir(path):
        if os.path.isfile(path + p):
            pics.append(p)
    return pics           

def resizeImage(path):
    for picName in searchImage(path):
        im = Image.open(path + picName)
        out = im.resize((640, 1136))
        out.save(path+'resize/' + picName)

if __name__ == '__main__':
    resizeImage("d:/workspace/show-me-the-code/0005atta/")