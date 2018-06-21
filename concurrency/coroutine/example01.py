#coding=utf-8
'''
Created on 2018年6月21日

@author: zwustudy

yield存入数据，通过for循环不断往外读出
'''

def fib():
    a, b = 0, 1
    while True and a < 100000:
        yield a
        a, b = b, a+b
        
for i in fib():
    print(i)

if __name__ == '__main__':
    pass