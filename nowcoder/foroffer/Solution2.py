'''
Created on 2018年1月17日
题目描述
输入一个链表，从尾到头打印链表每个节点的值。
知识点：链表
@author: minmin
'''
class ListNode:
    def __init__(self, x):
        self.val = x;
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        
        list1 = [listNode.val]
        while listNode.next != None: 
            listNode = listNode.next
            if listNode != None:
                list1.append(listNode.val)
                
        list1.reverse()                     
        return list1
    
    
if __name__ == '__main__':
    listNode0 = ListNode(0);
    listNode1 = ListNode(1);
    listNode2 = ListNode(2);
    listNode0.next = listNode1;
    listNode1.next = listNode2;
    print(Solution().printListFromTailToHead(listNode0));