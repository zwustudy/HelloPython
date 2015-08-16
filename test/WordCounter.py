#coding=utf-8
'''
Created on 2015年8月15日

@author: minmin
'''



if __name__ == '__main__':
    pass

file_obj = open('..\my father.txt')
try:
    all_the_text = file_obj.read()
finally:
    file_obj.close()
    
print all_the_text