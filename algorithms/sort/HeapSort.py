'''
Created on 2018年6月24日

@author: minmin
'''
def heapSort(array):
    if not array:
        return
    length = len(array) 
    start = length // 2 - 1
    for i in range(start, -1, -1):
        adjustHeap(array, i, len)
    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        adjustHeap(array, 0, i)
    
    
        
        
def adjustHeap(array, index, length):
    val = array[index]
    x = 2 * index + 1
    while x < length:
        if array[x] < array[x + 1] and x + 1 < length:
            x = x + 1
        if val < array[x]:
            array[x] = array[index]
            index = x
        x = x * 2 + 1
    array[index] = val
    
    
    
        
def testHeapSort():
    lst = [10,20,1,6,6,8,5,2,7,8,9]
    heapSort(lst);
    for x in lst:
        print(x)
 
if __name__ == '__main__':
    testHeapSort()