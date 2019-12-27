class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1024
        self.slots = [None] * self.size
        

    def add(self, key):
        slot = self.hashIt(key)
        if self.slots[slot] is None:
            self.slots[slot] = [key]
        else:
            if self.contains(key):
                return None 
            else:
                self.slots[slot].append(key)

    def remove(self, key):
        slot = self.hashIt(key)
        index = None
        if self.slots[slot] is None:
            return None 
        else:
            for i, v in enumerate(self.slots[slot]):
                if v == key:
                    index = i 
        if index is not None:
            self.slots[slot].pop(index)


    def contains(self, key):
        slot = self.hashIt(key)
        if self.slots[slot] is None:
            return False 
        else:
            for i, v in enumerate(self.slots[slot]):
                if v == key:
                    return True 
        return False 


    def hashIt(self, key):
        return key % self.size 
        