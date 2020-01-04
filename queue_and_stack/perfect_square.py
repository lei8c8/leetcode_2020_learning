class Solution:
    def numSquares(self, n: int) -> int:
        dp = [None] * (n + 1)
        if n == 1:
            return 1
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            value = float('inf')
            for j in range(1, i + 1):
                if j * j <= i:
                    value = min(value, dp[i-j*j] + 1) 
                else:
                    break
            dp[i] = value 
        return dp[-1]