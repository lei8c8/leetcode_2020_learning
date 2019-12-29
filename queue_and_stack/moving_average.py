from collections import deque 

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size 
        self.stream = deque()
        self.last_sum = 0
        
    def next(self, val: int) -> float:
        if len(self.stream) == self.size:
            tmp = self.stream.popleft()
            self.stream.append(val)
            self.last_sum = self.last_sum - tmp + val 
        else:
            self.stream.append(val)
            self.last_sum += val 
        return self.last_sum / len(self.stream)