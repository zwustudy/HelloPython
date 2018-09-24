'''
Created on 2018年1月28日
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
返回二维列表，内部每个列表表示找到的路径
@author: minmin
'''
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # 返回二维列表，内部每个列表表示找到的路径
    # 通过递归来实现，递归的关键是找到递归点，二叉树的结构本身是非常好的递归点，这题的关键是能够找到
    # 递归的时候和为expectNumber如何处理：递归后expectNumber = 递归前expectNumber - root.val
    def FindPathRecursion(self, root, expectNumer):
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumer:
            return [[root.val]]
        leftPath = self.FindPathRecursion(root.left, expectNumer - root.val)
        rightPath = self.FindPathRecursion(root.right, expectNumer - root.val)
        res = []
        for x in leftPath + rightPath:
            res.append([root.val] + x)
        return res
    
    # 返回二维列表，内部每个列表表示找到的路径
    # 通过遍历计算出所有的路径，遍历路径集合求和为expectNumber的所有路径
    # 使用到deque  double-end-queque是亮点
    def FindPathByTraversal(self, root, expectNumber):
        # write code here
        if not root:
            return []
        allPath = self.calculatePath(root)
        res = []
        for x in allPath:
            s = 0
            for i in x:
                s = s + i
            if s == expectNumber:
                res.append(x)
        return res
        
    def calculatePath(self, treeNode):
        if not treeNode.left and not treeNode.right:
            return [deque([treeNode.val])]
        leftPath = []
        rightPath = []
        if treeNode.left:
            leftPath = self.calculatePath(treeNode.left)
        if treeNode.right:
            rightPath = self.calculatePath(treeNode.right)
        for x in leftPath:
            x.appendleft(treeNode.val)
        for x in rightPath:
            x.appendleft(treeNode.val)
            leftPath.append(x)
        return leftPath