'''
Created on 2018年1月22日
题目描述：从第一级升级到第二级成功的概率是0.8,失败的概率是0.2，失败不降级；
从第二级升级到第三级的成功的概率是0.6,失败的概率是0.4,失败降一级；
从第三级升级到第四级的成功的概率是0.4,失败的概率是0.6,失败降一级；
从第四级升级到第五级的成功的概率是0.1,失败的概率是0.9,失败降一级；
升到第五级立即结束
现有100颗宝石，能够成功升到第五级的概率是多少？
每尝试一次升级消耗一颗宝石，请问从第一级升级到第五级需要的宝石期望是多少？
解答：
这是一个典型的动态规划的题目，问题的解要依赖于子问题的解的综合
其实求有限颗宝石之内，能够成功升级到某级的概率比较合适，
如果求从第一级升到第五级需要多少颗宝石，可以尝试100000次，得出结果取平均数大概在75-78之间的一个数字
@author: minmin
'''
import random


def getTryTimes():
    i = 1
    result = 0
    while (i < 5):
        number = random.randint(0, 9);
        result = result + 1
        mod = number % 10;
        if i == 1:
            if mod <= 1:
                i = 1
            else:
                i = 2
        elif i == 2:
            if mod <= 3:
                i = 1
            else:
                i = 3
        elif i == 3:
            if mod <= 5:
                i = 2
            else:
                i = 4
        elif i == 4:
            if mod <= 8:
                i = 3
            else:
                i = 5
    return result

def calculateRate(tryTimes):
    if tryTimes < 4:
        return 0;
    #rate = [[0] * 6] * (tryTimes + 1);
    rate = [([0] * 6) for i in range(tryTimes + 1)]
    rate[1][1] = 0.2
    rate[1][2] = 0.8
    for n in range(2, tryTimes + 1):
        for m in range(1, 6):
            rate[n][m] = calculate(rate, n, m)
            #print("%s,%s:%.6f" % (n, m, rate[n][m]))
    result = 0
    
    for i in range(1, tryTimes + 1):
        result = result + rate[i][5];
        #print("------%s,%s:%.20f" % (i, 5, rate[i][5]))
    
    return result
        
def calculate(rate, n, m):
    if m > n + 1:
        return 0
    if m == 1:
        return rate[n - 1][1] * 0.2 + rate[n - 1][2] * 0.4
    if m == 2:
        return rate[n - 1][1] * 0.8 + rate[n - 1][3] * 0.6
    if m == 3:
        return rate[n - 1][2] * 0.6 + rate[n - 1][4] * 0.9
    if m == 4:
        return rate[n - 1][3] * 0.4
    if m == 5:
        return rate[n - 1][4] * 0.1
if __name__ == '__main__':
    sum1 = 0
    testTimes = 10000
    for i in range(testTimes):
        times = getTryTimes()
        sum1 += times
    print(sum1/testTimes)
    
    rate = calculateRate(100)
    print("%.20f" % rate)
    
    
    