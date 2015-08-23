#coding=utf-8
'''
Created on 2015年8月23日

@author: minmin
'''
import random
import time
import myThread
import Queue
import threading

'''
生产者，每nsleep秒生产nprod个产品，放入queue中
a 产品标记
name 生产者的名字
'''
def producer(queue, nsleep, nprod, name, a, lock):
    while True:
        for i in range(nprod):
            lock.acquire()
            queue.put(a[0], 1)
            print '%s生产了一个产品：%d, 当前队列大小：%d' % (name, a[0], queue.qsize())
            a[0] += 1
            lock.release()
        time.sleep(nsleep)

'''
消费着，每nsleep秒从queue中消费minProd至maxProd间随机产生的一个值的产品
name 消费者的名字
'''
def consumer(queue, nsleep, minProd, maxProd, name):
    while True:
        nprod = random.randint(minProd, maxProd)
        for i in range(nprod):
            val = queue.get(1)    
            print '%s消费了一个产品：%d, 当前队列大小：%d' % (name, val, queue.qsize())
            
        time.sleep(nsleep)

def main():
    
    queue = Queue.Queue(10)
    a = [0]
    
    lock = threading.Lock()
    
    producer1 = myThread.MyThread(producer, (queue, 1, 1, 'producer1', a, lock), 'producer1')
    producer2 = myThread.MyThread(producer, (queue, 1, 2, 'producer2', a, lock), 'producer2')
    consumer1 = myThread.MyThread(consumer, (queue, 1, 1, 5, 'consumer1'), 'consumer1')
    threads = [producer1, producer2, consumer1]
    
    for i in threads:
        i.start()
        
    for i in threads:
        i.join()
    
if __name__ == '__main__':
    main()
    