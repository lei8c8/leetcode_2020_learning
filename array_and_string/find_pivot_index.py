class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        cum_total = 0
        for i, v in enumerate(nums):
            cum_total += v 
            if cum_total * 2 - v == total:
                return i
        return -1
