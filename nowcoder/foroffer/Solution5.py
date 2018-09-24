'''
Created on 2018年1月18日
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
@author: minmin
'''

class Solution:
    
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0:
            return 0
        elif length == 1:
            return rotateArray[0]
        left = 0
        right = length - 1;
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                #临界情况
                return rotateArray[right];
            middle = (left + right) / 2
            
            #三个顺序不能颠倒，因为第二个会用到第一个的排除情况
            if rotateArray[left] == rotateArray[middle] and rotateArray[right] == rotateArray[middle]:
                #无法判断在左边还是右边的情况
                return Solution.findMinByOrder(rotateArray, left, right)
            elif rotateArray[left] <= rotateArray[middle]:
                left = middle
            else:
                right = middle
        
        return rotateArray[middle]
    
    def findMinByOrder(self, rotateArray, left, right):
        m = rotateArray[left];
        for i in range(left + 1, right):
            if rotateArray[i] < m:
                return rotateArray[i]
            m = rotateArray[i];
        return rotateArray[left]