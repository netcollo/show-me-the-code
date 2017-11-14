#/usr/bin/env python

import os

# 读取目录下所有txt
def readText (path):
    for p in os.listdir(path):
        if os.path.isfile(path + p):
            #读取文件，计算单词
            pass
        

def countWords(fname):
    

if __name__ == '__main__':
    readText('./0006atta/')