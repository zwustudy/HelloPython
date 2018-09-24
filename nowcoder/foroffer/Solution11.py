'''
Created on 2018年2月1日

@author: minmin
'''

class Solution:
    
    def Permutation(self, ss):
        # write code herenot
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        charArr = list(ss)
        res = []
        for i in range(len(ss)):
            _str = "".join(charArr)
            if not _str in res:
                res.append(_str)
            for j in range(1,len(ss)):
                temp = charArr[j - 1]
                charArr[j - 1] = charArr[j]
                charArr[j] = temp
                _str = "".join(charArr)
                if not _str in res:
                    res.append(_str)
           
        res.sort()
        return res
    

if __name__ == "__main__":
    print(Solution().Permutation("aaABC"));



        