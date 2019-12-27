class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels, answer = set(J), 0
        for s in S:
            if s in jewels:
                answer += 1
        return answer
            
        