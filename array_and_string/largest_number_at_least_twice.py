class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, second_largest, index = -float('inf'), -float('inf'), None
        for i, v in enumerate(nums):
            if v > largest:
                second_largest = largest
                largest, index = v, i
            elif v > second_largest:
                second_largest = v
        return index if largest >= 2 * second_largest else -1