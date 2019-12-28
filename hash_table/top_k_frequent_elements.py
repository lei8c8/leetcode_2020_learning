from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = Counter(nums).most_common(k)
        return [pair[0] for pair in answer]
        