class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_set, res = set(nums1), set()
        for n in nums2:
            if n in my_set:
                res.add(n)
        return list(res)