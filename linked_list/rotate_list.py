class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head 
        k %= self.getListLen(head)
        if k == 0:
            return head
        prev, current = head, head 
        for i in range(k):
            current = current.next 
        while current.next:
            prev, current = prev.next, current.next
        new_head = prev.next 
        current.next = head 
        prev.next = None 
        return new_head 

    def getListLen(self, head):
        current, length = head, 0 
        while current:
            length += 1
            current = current.next
        return length
        