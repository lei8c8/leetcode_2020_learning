from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = defaultdict(list)
        for i, v in enumerate(nums):
            lookup[v].append(i)
        for i, v in enumerate(nums):
            if len(lookup[v]) > 1:
                for x in lookup[v]:
                    if 0 < abs(x - i) <= k:
                        return True 
        return False
   