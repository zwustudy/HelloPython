#coding=utf-8
'''
Created on 2015年8月16日

@author: minmin
'''

class Sample(object):
    '''
    classdocs
    '''
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, trace):
        print "type:", type
        print "value:", value
        print "trace:", trace
        
    def do_something(self):
        bar = 1 / 0
        return bar + 10

with Sample() as sample:
    sample.do_something() 


