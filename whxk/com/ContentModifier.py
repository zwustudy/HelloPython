'''
Created on 2018年4月18日

@author: minmin
'''
import os
from os import path

class ContentModifier:
    
    def modifier(self, rootDir):
       
        files = os.listdir(rootDir)
        for i in range(0, len(files)):
            path = os.path.join(rootDir, files[i])
            if os.path.isdir(path):
                print("dir:" + os.path.abspath(path))
                self.modifier(path)
            if os.path.isfile(path):
                print("file:" + os.path.abspath(path))

if __name__ == '__main__':
    rootDir = "D:\work\武汉新科\_\_"
    ContentModifier().modifier(rootDir)