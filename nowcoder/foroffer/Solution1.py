'''
Created on 2018年1月20日
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则返回True,否则返回False。假设输入的数组的任意两个数字都互不相同。
@author: minmin
'''
class Solution:
    
    '''
          递归实现
    '''
    def VerifySquenceOfBSTByRecursion(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        r = sequence[-1]
        i = 0
        while i < len(sequence):
            if sequence[i] < r:
                i = i + 1
            else:
                break
        leftSequence = sequence[0:i]
        rightSequence = sequence[i:len(sequence) - 1]
        for x in rightSequence:
            if x < r:
                return False
        left = True
        right = True
        if len(leftSequence) > 1:
            left = self.VerifySquenceOfBSTByRecursion(leftSequence)
        if len(rightSequence) > 1:
            right = self.VerifySquenceOfBSTByRecursion(rightSequence)
        return left and right
    
    '''
           非递归实现
    '''
    def VerifySquenceOfBSTByNotRecursion(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        i = len(sequence) - 1
        while i >= 2:
            j = 0
            while j <= i:
                if sequence[j] > sequence[i]:
                    break
                else:
                    j = j + 1
            rightS = sequence[j:i]
            for x in rightS:
                if x < sequence[i]:
                    return False
            i = i - 1
        return True
    
if __name__ == "__main__":
    sequence = [1,2,3,10,20,13,12]
    print(Solution().VerifySquenceOfBSTByNotRecursion(sequence))