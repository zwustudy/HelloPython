'''
Created on 2018年6月24日

@author: zwustudy
'''
def heapSort(array):
    if not array:
        return
    length = len(array) 
    start = length // 2 - 1
    """构建大顶堆
    """
    for i in range(start, -1, -1):
        adjustHeap(array, i, length)
    """取走堆顶，放到数组最后，把数组最后一个元素放到堆顶，让其下沉，调整成大顶堆
    """
    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        adjustHeap(array, 0, i)
     
"""进行堆调整
"""   
def adjustHeap(array, index, length):
    x = 2 * index + 1
    while x < length:
        if array[x] < array[x + 1] and x + 1 < length:
            x = x + 1
        if array[index] < array[x]:
            """大数往上调整，小数往下调整
            """
            array[index], array[x] = array[x], array[index]
            index = x
        x = x * 2 + 1
        
def testHeapSort():
    lst = [10,20,1,6,6,8,5,2,7,8,9]
    heapSort(lst);
    for x in lst:
        print(x)
 
if __name__ == '__main__':
    testHeapSort()