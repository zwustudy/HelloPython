#coding=utf-8
'''
Created on 2015年8月14日

@author: zwustudy
1、输出所有小于等于max的质数，这里提供两种方法:
    producePrime1使用质数判断方法，一直遍历到某一个数的平方根值
    producePrime2使用筛选法，筛选剔除小于等于max的所有非质数，剩下的就是质数了
2、从小到大，输出前m个质数。  筛法的速度远超普通方法，针对这个需求，普通方法很慢，筛法又不适用，因为不知道前m个质数对应的max是多少，
  这怎么办呢？质数越往后越稀疏，有个素数定理就是用来预估max以内有多少质数，最简洁的公式有x/ln(x)，会有一定的误差，但是不超过百分之十五
 那么我们可以根据m反推出max的大小
'''
import math
import time


'''
   最朴素的判断质数的方法， 即根据质数的定义，一直从2到该数的平方根，判断是否能整除
'''    
def producePrime1(max):
    for i in range(2, max + 1):
        if __isPrime(i): print i

'''
筛选法找质数，即“埃拉托色尼筛法”，挖掉2的倍数、3的倍数、一直到max的平方根的倍数，剩下的都是质数了
'''          
def producePrime2(max):
    li = []
    for i in range(2, max + 1):
        if i > 2 and i % 2 == 0:
            li.append(0)
        else:
            li.append(i)
    
    for i in range(3, int(math.sqrt(max)) + 1, 2):
        if li[i - 2] != 0:
            for j in range(i + i, max + 1, i):
                li[j - 2] = 0
    
    for i in li:
        if i != 0:
            print i  

'''
从小到大，输出前count(count > 10)个质数
这里先使用素数定理求出count个素数分布的范围，再使用筛选法筛除所有素数，最后输出前count个素数
'''
def producePrePrime(count):
    max = int(__findMax(count) * 1.15)
    li = []
    for i in range(2, max + 1):
        if i > 2 and i % 2 == 0:
            li.append(0)
        else:
            li.append(i)
    
    for i in range(3, int(math.sqrt(max)) + 1, 2):
        if li[i - 2] != 0:
            for j in range(i + i, max + 1, i):
                li[j - 2] = 0
    
    j = 0
    for i in li:
        if i != 0:
            print i
            j += 1
            if j >= count:
                break  
    
        

'''
    判断number是否是质数
'''
def __isPrime(number):
    if number <= 1 : return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0 :
            return False
    return True 

'''
根据素数定理，x/ln(x) >= m 找到最小的一个整数x解，m > 10
'''
def __findMax(m):
    if m <= 10:
        raise NameError('input illeagal m <= 10!')
    
    start = m
    end = m * 2
    while True:
        if end / math.log(end,math.e) >= m:
            break;
        start = end
        end = end * 2
    index = int((start + end) / 2)
    while True:
        m1 = index / math.log(index, math.e)
        m2 = (index - 1) / math.log(index - 1, math.e)
        if m1 >= m and m2 < m:
            break;
        if m1 >= m:
            end = index
        else:
            start = index
        index = int((start + end) / 2)
        
    return index

max = 1000000
        
start = long(time.time() * 1000)    
producePrime1(max)
end1 = long(time.time() * 1000)
producePrime2(max)
end2 = long(time.time() * 1000)

producePrePrime(10000)

print("使用质数定义法找出所有小于等于" + str(max) + "质数并输出，总共耗时" + str(end1 - start) + "毫秒")   
print("使用筛选法找出所有小于等于" + str(max) + "质数并输出，总共耗时" + str(end2 - end1) + "毫秒")
    