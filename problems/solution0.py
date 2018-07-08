'''
Created on 2018年7月8日

描述：输入一个正整数，求其二进制表示的1的个数；
可以利用这样一个事实，二进制表示为AAAAAB，B为最后一位，AAAAA为正整数除以2向下取整
这样就可以递归求解出正整数中1的个数

@author: zwustudy
'''

def count_one(num):
    if num < 2:
        return num
    return num % 2 + count_one(num >> 1)

def main():
    for x in range(0, 11):
        print(str(x) + "二进制表示中1的个数有：" + str(count_one(x)))

if __name__ == '__main__':
    main();