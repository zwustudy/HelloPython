#coding=utf-8
'''
Created on 2015年8月23日

@author: minmin
'''
from myThread import MyThread
import time

def fib(index):
    time.sleep(0.005)
    if index < 2: return 1
    return fib(index - 1) + fib(index - 2)

def fac(index):
    time.sleep(0.1)
    if index < 2: return 1
    return index * fac(index - 1)

def sum(index):
    time.sleep(0.1)
    if index < 2: return 1
    return index + sum(index - 1)

def main():
    
    funcs = [fib, fac, sum]
    n = 12
    nfuncs = range(len(funcs))
    
    print '*** SINGLE THREAD all starting at:%s ***' % time.strftime('%Y-%m-%d %H:%M:%S')
    for i in nfuncs:
        print 'starting %s, at:%s' % (funcs[i].__name__, time.strftime('%Y-%m-%d %H:%M:%S'))
        print funcs[i](n)
        print '%s finished at:%s' % (funcs[i].__name__, time.strftime('%Y-%m-%d %H:%M:%S'))
        
    print '*** SINGLE THREAD all done at:%s ***' % time.strftime('%Y-%m-%d %H:%M:%S')
    
    print '*** MULTIPLE THREAD all starting at:%s ***' % time.strftime('%Y-%m-%d %H:%M:%S')
        
    threads = []
    for i in nfuncs:
        thread = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(thread)
    
    for i in threads:
        i.start()
        
    for i in threads:
        i.join()
        print i.getResult()
        
    print '*** MULTIPLE THREAD all starting at:%s ***' % time.strftime('%Y-%m-%d %H:%M:%S')
if __name__ == '__main__':
    main()