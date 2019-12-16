class Solution:
    def twoSum(self, numbers, target):
        lookup = {}
        for i, v in numbers:
            lookup[v] = i 
        for i, v in enumerate(numbers):
            if (target - v) in lookup and lookup[target - v] != i:
                return [v, lookup[target - v]]