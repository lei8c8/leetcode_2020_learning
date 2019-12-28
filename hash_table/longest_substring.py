class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, seen, ans = 0, 0, set(), 0 
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                ans = max(ans, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return ans

