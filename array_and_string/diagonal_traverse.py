from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []
        res, mydict = [], defaultdict(list)
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                mydict[i+j].append(matrix[i][j])
        for i in range(len(mydict)):
            if i % 2 == 0:
                mydict[i] = mydict[i][::-1]
            res.extend(mydict[i])
        return res 
