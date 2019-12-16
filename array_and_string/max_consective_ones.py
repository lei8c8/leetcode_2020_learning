class Solution:
    def findMaxConsecutiveOnes(self, nums):
        left, m, c= 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c = (i - left) + 1
                m = max(m, c)
            else:
                left = i + 1
        return m