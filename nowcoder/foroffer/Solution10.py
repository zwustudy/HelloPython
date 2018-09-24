'''
Created on 2018年1月30日
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
@author: minmin
'''

class Solution10:
  
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        if pRootOfTree.right:
            #如果右节点存在，通过递归找到右节点链表的首节点，将其与pRootOfTree连接起来
            rightNode = self.Convert(pRootOfTree.right)
            rightNode.left = pRootOfTree
            pRootOfTree.right = rightNode
            
        if pRootOfTree.left:
            #如果左节点存在，通过递归找到左节点链表的尾节点，将其与pRootOfTree连接起来
            leftNode = self.Convert(pRootOfTree.left)
            leftNode_last = self.FindLastNode(leftNode)
            leftNode_last.right = pRootOfTree
            pRootOfTree.left = leftNode_last
            return leftNode
        else:
            #如果左节点不存在，则说明pRootOfTree已经是首节点了
            return pRootOfTree
    
    def FindLastNode(self, treeNode):
        if not treeNode:
            return None
        while treeNode.right:
            treeNode = treeNode.right
        return treeNode