#coding=utf-8
'''
Created on 2015年8月23日

@author: zwustudy
'''
import threading
import time

class MyThread(threading.Thread):

    def __init__(self, func, args, name = ''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
        
    def getResult(self):
        return self.res
    
    def run(self):
        print('starting %s at:%s' % (self.name, time.strftime('%Y-%m-%d %H:%M:%S')))
        #self.res = apply(self.func, self.args)
        self.res = self.func(*self.args)
        print('%s finished at:%s' % (self.name, time.strftime('%Y-%m-%d %H:%M:%S')))
        