class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, v in enumerate(nums):
            hashMap[v] = i
        for i, v in enumerate(nums):
            if (target - v) in hashMap and hashMap[target - v] != i:
                return [i, hashMap[target - v]]