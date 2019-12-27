class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        hashMap1, hashMap2 = {}, {}
        for i in range(len(s)):
            if s[i] not in hashMap1:
                hashMap1[s[i]] = t[i]
            if t[i] not in hashMap2:
                hashMap2[t[i]] = s[i]
            if hashMap1[s[i]] != t[i] or hashMap2[t[i]] != s[i]:
                return False 
        return True 
