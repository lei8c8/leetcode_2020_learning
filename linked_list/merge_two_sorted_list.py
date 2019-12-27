class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1 
        node = ListNode(0)
        head = node 
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                node = l1 
                l1 = l1.next 
            else:
                node.next = l2
                node = l2
                l2 = l2.next 
        if l1:
            node.next = l1 
        if l2:
            node.next = l2 
        head = head.next 
        return head 

