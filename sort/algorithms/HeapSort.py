'''
Created on 2018年3月25日

@author: zwustudy
'''

class HeapSort:
    
    def sort(self, lst):
        if not lst:
            return False
        length = len(lst)
        start = length // 2 - 1  #地板除，为了取到整数
        for x in range(start, -1, -1):
            self.adjustHeap(lst, x, length)
        index = length - 1
        for x in range(index, 0, -1):
            self.swap(lst, x, 0)
            #因为只是把大顶堆的堆顶元素和最后一个元素进行交换了，整个堆只有第一个元素是不合求的，因此只需要
            #把第一个元素沉下去
            self.adjustHeap(lst, 0, x)
                   
    '''
          使用异或运算交换元素的值
    '''
    def swap(self, lst, i, j):
        if lst[i] == lst[j]:
            return
        lst[j] ^= lst[i]
        lst[i] ^= lst[j] 
        lst[j] ^= lst[i] 
    
    '''
          建立大顶堆
    '''
    def adjustHeap(self, lst, index, length):
        
        value = lst[index]
        x = 2 * index + 1
        while x < length:
            if x + 1 < length and lst[x] < lst[x + 1]:
                x += 1
            if value < lst[x]:
                lst[index] = lst[x]
                index = x
            x = 2 * x + 1
        lst[index] = value
        
        
        
             
            
            
        
        
        