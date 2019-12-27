from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = defaultdict(list)
        for i, v in enumerate(nums):
            lookup[v].append(i)
        for i, v in enumerate(nums):
            for x in lookup[v]:
                if x == i:
                    continue
                if abs(x - i) <= k:
                    return True 
        return False
   