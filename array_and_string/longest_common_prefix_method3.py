class Solution:
    def longestCommonPrefix(self, strs):
        if  len(strs) == 0: return ""
        c = 0
        for i in range(len(strs[0])):
            try:
                tmp = [(x[i] == strs[0][i]) for x in strs]
                if all(tmp):
                    c += 1
                else: 
                    break
            except IndexError:
                break
        return strs[0][:c]