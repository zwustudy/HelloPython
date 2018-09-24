'''
Created on 2018年1月28日
题目描述：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

解题思路:这题的难点在于如何给节点的random引用如何赋值
可以这样操作：
第一步：在链表中每一个节点后面都插入一个赋值节点A->B->C改为A->A1->B->B1->C->C1
第二步：把A的random节点下一个节点赋值给A1的random引用。这样巧妙的利用了上面的结构
不用去找出来random节点到底是哪个，因为random节点的下一个节点就刚好是我们构造出来的Random1节点
第三步：按照奇偶拆分两个链表
@author: minmin
'''
class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    
    #返回RandomListNode的头结点
    def Clone(self, pHead):
        if not pHead:
            return None
        old = pHead
        while pHead:
            old_next = pHead.next
            new_next = RandomListNode(pHead.val)
            pHead.next = new_next
            new_next.next = old_next
            pHead = old_next
        pHead = old
        while pHead:
            old_random = pHead.random
            new_next = pHead.next
            if old_random:
                new_next.random = old_random.next
            pHead = new_next.next
        pHead = old
        new = pHead.next
        while pHead:
            new_next = pHead.next
            old_next = new_next.next
            pHead.next = old_next
            if old_next:
                new_next.next = old_next.next
            pHead = old_next
        return new

if __name__ == "__main__":
    pHead = RandomListNode(100);
    
    pHead.next = RandomListNode(200);
    
    print(Solution().Clone(pHead).val)

        
            
            
            
            
            
            