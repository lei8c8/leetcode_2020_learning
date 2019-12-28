from collections import defaultdict

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hashmap, answer = defaultdict(int), 0
        for a in A:
            for b in B:
                hashmap[a+b] += 1
        for c in C:
            for d in D:
                target = 0 - c - d 
                answer += hashmap[target]
        return answer
