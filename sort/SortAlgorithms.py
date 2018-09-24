'''
Created on 2018年3月25日

@author: minmin
'''
from sort.algorithms import HeapSort

def testHeapSort():
    lst = [10,20,1,6,6,8,5,2,7,8,9]
    HeapSort.HeapSort().sort(lst);
    for x in lst:
        print(x)
 
if __name__ == '__main__':
    testHeapSort()