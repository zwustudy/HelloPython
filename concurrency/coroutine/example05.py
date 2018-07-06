'''
<<<<<<< HEAD
Created on 2018年6月21日

@author: zwustudy
'''
import random
import time

def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_cnt = yield b
        print('let me think {0} secs'.format(sleep_cnt))
        time.sleep(sleep_cnt)
        a, b = b, a + b
        index += 1
print('-'*10 + 'test yield send' + '-'*10)
N = 20
sfib = stupid_fib(N)
fib_res = next(sfib)
while True:
    print(fib_res)
    try:
        fib_res = sfib.send(random.uniform(0, 0.5))
    except StopIteration:
        break

if __name__ == '__main__':
    pass
=======
Created on 2018年6月23日

@author: zwustudy
'''

from greenlet import greenlet
import time


def test1():
    while True:
        print("---我是A函数--")
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print("---我是B函数--")
        gr1.switch()
        time.sleep(0.5)


def main():
    # 切换到gr1中运行
    gr1.switch()


if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    main()
>>>>>>> 24c33f5f978ec73fcee812e2f472b20a7da274bb
