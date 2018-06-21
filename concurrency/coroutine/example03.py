'''
Created on 2018年6月21日

@author: zwustudy

作为filter使用，
follow将file中的每一行读取，send到coroutine中，grep查找匹配的line，send到下一个coroutine中，printer接收send过来的data，并且输出。 完成整个filter的流程。
follow()-> grep() : send() 
grep() -> printer():send()
'''
import asyncio
import time

def follow(thefile, target):
    #thefile.seek(0,2) # Go to the end of the file
    next(target)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        target.send(line)
 
@asyncio.coroutine
def printer():
    while True:
        line = (yield)
        print(line)
    
@asyncio.coroutine
def grep(pattern, target):
    next(target)
    while True:
        line = (yield) # Receive a line
        if pattern in line:
            print(line)
            target.send(line) # Send to next stage
            

if __name__ == '__main__':
    f = open("my father.txt")
    target3 = follow(f, grep('the', printer()))
    pass