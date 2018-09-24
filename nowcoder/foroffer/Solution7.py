'''
Created on 2018年1月28日
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1
是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）

借助一个栈实现，push进元素，如果栈顶元素等于pop序列的第一个，就出栈。
如果最后栈为空，则说明是。两个序列的长度要满足相等
@author: minmin
'''

class Solution:
    
    '''
          解题思路：借助一个栈实现，push进元素，如果栈顶元素等于pop序列的第一个，就出栈。
          如果最后栈为空，则说明是。两个序列的长度要满足相等
    '''
    def isPopOrder(self, pushV, popV):
        if len(pushV) != len(popV):
            return False
        stack = []
        index = 0
        for x in pushV:
            stack.append(x);
            while stack[-1] == popV[index]:
                stack.pop()
                index = index + 1
        return len(stack) == 0
        
    
        