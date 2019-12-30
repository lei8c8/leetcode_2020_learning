class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.size = 0
        self.min_val = float('inf')
        

    def push(self, x: int) -> None:
        self.data.append(x)
        self.size += 1
        if self.min_val > x:
            self.min_val = x
        

    def pop(self) -> None:
        if self.isEmpty():
            raise IndexError
        value = self.data.pop()
        self.size -= 1
        if value == self.min_val:
            if not self.isEmpty():
                self.min_val = min(self.data)
            else:
                self.min_val = float('inf')
        

    def top(self) -> int:
        if self.isEmpty():
            raise IndexError
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.min_val if not self.isEmpty() else None


    def isEmpty(self):
        return self.size == 0