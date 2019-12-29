class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.items = [None for i in range(k)]
        self.size = 0
        self.capacity = k
        self.head = 0
        self.tail = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.items[self.tail] = value 
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True 
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False 
        self.items[self.head] = None 
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True 
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity