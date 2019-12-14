class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(y) for y in list(str(int(''.join([str(x) for x in digits])) + 1))]