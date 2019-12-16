class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        total = 0
        for i, v in enumerate(nums):
            if i % 2 == 0:
                total += v
        return total