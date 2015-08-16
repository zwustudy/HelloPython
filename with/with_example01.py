#coding=utf-8
'''
Created on 2015年8月16日

#with_sample
@author: minmin
'''

class Sample(object):
    '''
    classdocs
    '''
    def __enter__(self):
        print "In __enter__ function"
        return "Foo"
    
    def __exit__(self, type, value, trace):
        print "In __exit__ function"

    def __init__(self):
        print "In __init__ function"
        
def get_sample():
    return Sample()


with get_sample() as sample:
    print "Sample:", sample

