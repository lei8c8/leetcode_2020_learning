class Solution:
    def removeDuplicates(self, nums):
        k = 0 
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k = k + 1
                nums[k] = nums[i]
        return k + 1

        