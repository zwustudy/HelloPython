#coding=utf-8
'''
Created on 2015年8月23日

@author: minmin
'''

import threading
import time

class MyThread(threading.Thread):
    
    def __init__(self, func, args, name = ''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        
    def run(self):
        apply(self.func, self.args)
        

def loop(nloop, nsleep):
    print "start loop%d at:%s" % (nloop, time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(nsleep)
    print "loop%d done at:%s" % (nloop, time.strftime('%Y-%m-%d %H:%M:%S'))


def main():
    print "starting at:%s" % time.strftime('%Y-%m-%d %H:%M:%S')
    loops = [4, 2]
    nloops = range(len(loops))
    
    threads = []
    
    for i in nloops:
        thread = MyThread(loop, (i, loops[i]))
        threads.append(thread)
        
    for i in threads:
        i.start()
        
    for i in threads:
        i.join()
        
    print "all done at:%s" % time.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    main()