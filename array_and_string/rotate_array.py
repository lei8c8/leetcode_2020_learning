class Solution:
    def rotate(self, nums, k):
        k %= len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


        