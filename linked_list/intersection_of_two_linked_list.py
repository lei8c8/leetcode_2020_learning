# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        cA, cB = 0, 0
        if not headA or not headB:
            return None 
        while True:
            if curA == curB:
                return curA
            if curA.next:
                curA = curA.next 
            else:
                curA = headB 
                cA += 1
            if curB.next:
                curB = curB.next 
            else:
                curB = headA
                cB += 1
            if cA > 1 or cB > 1:
                return None