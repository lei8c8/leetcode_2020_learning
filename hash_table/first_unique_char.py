from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ct = Counter(s)
        for i, v in enumerate(s):
            if ct[v] == 1:
                return i
        return -1