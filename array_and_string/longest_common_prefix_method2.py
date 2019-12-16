class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        c = 0
        for i in range(len(strs[0])):
            try:
                tmp = [x[i] for x in strs]
            except IndexError:
                break 
            if len(set(tmp)) == 1:
                c += 1
            else: 
                break
        return strs[0][:c]