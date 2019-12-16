class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        res, element_number = 0, len(strs)
        max_loop_number = min([len(x) for x in strs])
        for i in range(max_loop_number):
            compare_char, all_the_same = strs[0][i], True
            for j in range(1, element_number):
                if strs[j][i] != compare_char:
                    all_the_same = False
                    break
            if not all_the_same:
                return strs[0][:res]
            else:
                res += 1
        return strs[0][:element_number]

