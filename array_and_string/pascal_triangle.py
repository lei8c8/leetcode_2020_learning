class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        res = [[] for _ in range(numRows)]
        for i in range(numRows):
            if i == 0:
                res[i] = [1]
            else:
                for j in range(i+1):
                    if j == 0 or j == i:
                        res[i].append(1)
                    else:
                        res[i].append(res[i-1][j-1] + res[i-1][j])
        return res

