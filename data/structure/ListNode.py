'''
Created on 2018年6月25日

单向链表
打印方法
提供逆置的方法，两种实现迭代和递归

@author: zwustudy
'''
class ListNode(object):

    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt
        
    """单向链表打印
    """
    def toString(self):
        if not self.nxt:
            return str(self.val)
        return str(self.val) + " " + self.nxt.toString()
    
    """单向链表逆置
    """
    def reverse(self):
        node = self
        if not node.nxt:
            return node
        
        """A->B->C->D
        """
        nxt = node.nxt
        node.nxt = None#取到B，把A断开
        
        """A<-B  C->D
        """
        while nxt:
            nextnext = nxt.nxt #取到B的下一个节点
            nxt.nxt = node #由于已经获得了下一个节点的引用，这里可以放心大胆的把B的下一个节点指向当前的头节点，
            node = nxt #把B赋值给头结点，这样就node永远表示已经逆置的部分的头结点
            nxt = nextnext #之前持有的下一个节点的引用，继续往下遍历
        return node
    
    """通过递归来实现，只是不是尾递归
    """
    def reverse_by_recursive(self):
        
        node = self
        if not node.nxt:
            return node
        
        """
        A->B->C->D
        """        
        result = node.nxt.reverse();
        node.nxt.nxt = node #C的next是D，也就是操作把D的next指向C。
        node.nxt = None
        """处理成：A->B->C<-D的结构，C不指向。每递归一层，这样的截点就往前走一步，最后直到A<-B<-C<-D
        """
        return result
    
def main():
    
    """通过循环的方式创建单向链表
    """
    node = None
    for x in range(3, 0 , -1):
        node = ListNode(x, node);
    
    print(node.toString())
    node = node.reverse();
    print(node.toString())
    print(node.reverse_by_recursive().toString())
if __name__ == "__main__":
    main()