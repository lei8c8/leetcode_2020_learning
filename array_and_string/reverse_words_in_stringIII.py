class Solution:
    def reverseWords(self, s):
        s = s.split()
        for i, v in enumerate(s):
            s[i] = v[::-1]
        return ' '.join(s)
