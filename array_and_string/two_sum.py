class Solution:
    def twoSum(self, numbers, target):
        lookup = {}
        for i, v in enumerate(numbers):
            lookup[v] = i 
        for i, v in enumerate(numbers):
            if (target - v) in lookup and lookup[target - v] != i:
                return [i + 1, lookup[target - v] + 1]