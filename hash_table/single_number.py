class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_set = set()
        for num in nums:
            if num in my_set:
                my_set.remove(num)
            else:
                my_set.add(num)
        return my_set.pop()