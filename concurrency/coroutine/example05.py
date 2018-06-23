'''
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