class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        return len(haystack.split(needle)[0]) if needle in haystack else -1
        