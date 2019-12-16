class Solution:
    def minSubArrayLen(self, s, nums):
        left, res, total = 0, float('inf'), 0
        for right in range(len(nums)):
            total += nums[right]
            while (total >= s):
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return res if res != float('inf') else 0 