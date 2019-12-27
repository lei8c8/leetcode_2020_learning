# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if not head: return head
        current, node = head, None
        while current.next:
            node = current.next 
            current.next = current.next.next
            node.next = head 
            head = node 
        return head 