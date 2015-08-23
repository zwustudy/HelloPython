#coding=utf-8
'''
Created on 2015年8月19日

@author: minmin
'''

import  threading
import time

loops = [4, 2]

class ThreadFunc(object):
    
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args
        
    def __call__(self):
        #大于1.6的版本下面一句可以这样写  self.res = self.func(*self.args)
        apply(self.func, self.args)


def loop(nloop, nsleep):
    print "start loop" + str(nloop) + " at:" + time.ctime()
    time.sleep(nsleep)
    print "loop" + str(nloop) + " done at:"+  time.ctime()
    

def main():
    print "starting at:", time.ctime()
    threads = []
    
    nloops = range(len(loops))
    
    for i in nloops:
        thread = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(thread)
        
    for i in threads:
        i.start()
        
    for i in threads:
        i.join()
        
    print "all done at:", time.ctime()
    
if __name__ == '__main__':
    main()