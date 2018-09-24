'''
Created on 2018年1月27日
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 
[[1,2,3,4]
 [5,6,7,8]
 [9,10,11,12]
 [13,14,15,16]] 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
@author: minmin
'''

class Solution6:

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            res.append(matrix[0][0])
            return res
        a = 0
        b = 0
        c = m - 1
        d = n - 1
        i = 0
        print(m)
        print(n)
        while c >= a and d >= b:
            for i in range(b, d + 1):
                if c < a:
                    break
                res.append(matrix[b][i])
            a = a + 1
            for i in range(a, c + 1):
                if d < b:
                    break
                res.append(matrix[i][d])
            d = d - 1
            for i in range(d, b - 1, -1):
                if c < a:
                    break
                res.append(matrix[c][i])
            c = c - 1
            for i in range(c, a - 1, -1):
                if d < b:
                    break
                res.append(matrix[i][b])
            b = b + 1
        return res
    
if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    res = Solution6().printMatrix(matrix)
    for x in res:
        print(x)
    