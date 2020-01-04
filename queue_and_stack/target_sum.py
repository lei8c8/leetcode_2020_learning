class Solution:
    def __init__(self):
        self.count = 0
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.helper(nums, 0, 0, S)
        return self.count

    def helper(self, nums, i, total, S):
        if i == len(nums):
            if S == total:
                self.count += 1
        else:
            self.helper(nums, i + 1, total + nums[i], S)
            self.helper(nums, i + 1, total - nums[i], S)
        
