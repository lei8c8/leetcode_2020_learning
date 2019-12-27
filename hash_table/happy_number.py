class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            s = 0
            if n in seen:
                return False
            elif n == 1:
                return True 
            else:
                seen.add(n)
                tmp = self.toDigits(n)
                for t in tmp:
                    s += t ** 2
                n = s
    
    def toDigits(self, x):
        tmp = [int(y) for y in str(x)]
        return tmp

        