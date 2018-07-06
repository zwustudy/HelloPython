'''
Created on 2018年6月24日

@author: minmin
'''
    
def quick_sort_algorithms(array, l ,r):
    if l < r:
        x = array[r]
        i = l - 1
        for j in range(l, r):
            if array[j] < x:
                i += 1
                array[j], array[i] = array[i], array[j]
        array[i + 1], array[r] = array[r], array[i + 1]           
        quick_sort_algorithms(array, l, i)
        quick_sort_algorithms(array, i + 2, r)
        
def quick_sort_usual(array, l, r):
    if l >= r:
        return
    low = l
    high = r
    x = array[low]
    while low < high:
        while low < high and array[high] >= x:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] <= x:
            low += 1
        array[high] = array[low]
    array[high] = x
    quick_sort_usual(array, l, low - 1)
    quick_sort_usual(array, low + 1, r)
    
def sort0(array, l, r):
    if l >= r:
        return
    key = array[r]
    i = l - 1
    for x in range(l, r):
        if array[x] < key:
            i += 1
            array[i], array[x] = array[x], array[i]
    array[i + 1], array[r] = array[r], array[i + 1] 
    
    #递归的深度不变，但是栈的深度有优化
    if 2 * i >= r:
        sort0(array, i + 2, r)
        sort0(array, l, i)
    else:
        sort0(array, l, i)
        sort0(array, i + 2, r)
        
def main():
    
    array = [10,20,1,6,6,8,5,2,7,8,9]
    sort0(array, 0, len(array) - 1)
    for x in array:
        print(x)
        
if __name__ == "__main__":
    main()
        

        
         
      
    
            

        