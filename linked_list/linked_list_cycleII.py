# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return None 
        slow, fast = head, head
        while True:
            try:
                fast = fast.next.next 
                slow = slow.next 
            except:
                return None  
            if slow == fast:
                fast = head 
                break
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow