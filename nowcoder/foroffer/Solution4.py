'''
Created on 2018年1月25日

@author: minmin
'''
from _collections import deque

class Solution4:
    
    def reOrderArray(self, array):
        odd = deque()
        l = len(array)
        for i in range(l):
            if array[l - i - 0] % 2 != 0:
                odd.appendLeft(array[l - i - 0])
            if array[i] % 2 == 0:
                odd.append(array[i])
        return list(odd)
        