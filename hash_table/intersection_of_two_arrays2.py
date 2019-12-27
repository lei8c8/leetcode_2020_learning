from collections import Counter 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ct, res = Counter(nums1), []
        for n in nums2:
            if n in ct and ct[n] > 0:
                res.append(n)
                ct[n] -= 1
        return res 