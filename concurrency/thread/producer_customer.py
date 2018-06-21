#coding=utf-8
'''
Created on 2015年8月19日

设计三个线程，线程1每秒钟对一个值进行+1操作，线程2每秒钟对该值进行+3操作，线程3每秒钟对该值进行-2操作

@author: minmin
'''
import time
import thread

def loop(name, value, nsleep, action, lock1, lock2):
    
    while True:
        lock1.acquire()
        value[0] += action
        action_str = ""
        if action >= 0:
            action_str = "+" + str(action)
        else:
            action_str = str(action) 
        
        print name + "对value做了" + action_str + "操作， value = " + str(value[0])
        lock1.release()
        time.sleep(nsleep)

    lock2.release()

def main():

    lock = thread.allocate_lock()
    lock1 = thread.allocate_lock()
    lock2 = thread.allocate_lock()
    lock3 = thread.allocate_lock()
    
    value = [10]
    
    lock1.acquire()
    lock2.acquire()
    lock3.acquire()
    
    locks = [lock1, lock2, lock3]
    
    thread.start_new_thread(loop, ("Producer1", value, 1, 1, lock, lock1))
    thread.start_new_thread(loop, ("Producer2", value, 1, 3, lock, lock2))
    thread.start_new_thread(loop, ("Customer1", value, 1, -2, lock, lock3))    

    #防止主线程执行完自动关闭运行的三个线程
    for i in locks:
        while i.locked(): pass

if __name__ == '__main__':
    main()

