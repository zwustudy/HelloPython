'''
Created on 2018年4月16日
按层序打印二叉树                    A
            B               C
      D           E               F
输出：
A
B,C
D,E,F
@author: minmin
'''
class TreeNode:
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class Solution12:
    
    def printTree(self, root):
        if not root:
            return False
        nodeList = [root]
        size = len(nodeList)
        last = 0
        i = 0
        while i < len(nodeList):
            print(nodeList[i].value, end="")
            if i == size - 1:
                print()
                for j in range(last, size):
                    if nodeList[j].left:
                        nodeList.append(nodeList[j].left)
                    if nodeList[j].right:
                        nodeList.append(nodeList[j].right)
                last = size
                size = len(nodeList)
            i += 1

if __name__ == '__main__':
    
    d = TreeNode('D', None, None)
    e = TreeNode('E', None, None)
    f = TreeNode('F', None, None)
    
    b = TreeNode('B', d, e)
    c = TreeNode('C', None, f)
    
    a = TreeNode('A', b ,c)
    
    Solution12().printTree(a)
    