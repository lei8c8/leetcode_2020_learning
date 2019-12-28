class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items_count = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.items_count:
            self.items_count[number] = 1
        else:
            self.items_count[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key in self.items_count:
            target = value - key
            if target != key:
                if target in self.items_count:
                    return True
            else:
                if self.items_count[target] > 1:
                    return True
        return False