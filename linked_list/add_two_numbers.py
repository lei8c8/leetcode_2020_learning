class Solution:
    def addTwoNumbers(self, l1, l2):
        l1current, l2current = l1, l2 
        prev, addOne = ListNode(-1), 0
        before_head = prev
        while l1current and l2current:
            hereVal = (l1current.val + l2current.val + addOne) % 10
            if l1current.val + l2current.val + addOne > 9:
                addOne = 1
            else:
                addOne = 0
            node = ListNode(hereVal)
            prev.next = node 
            prev = node 
            l1current, l2current = l1current.next, l2current.next
        while l1current:
            hereVal = (l1current.val + addOne) % 10
            if l1current.val + addOne > 9:
                addOne = 1
            else:
                addOne = 0 
            node = ListNode(hereVal)
            prev.next = node 
            prev = node 
            l1current = l1current.next 
        while l2current:
            hereVal = (l2current.val + addOne) % 10
            if l2current.val + addOne > 9:
                addOne = 1
            else:
                addOne = 0 
            node = ListNode(hereVal)
            prev.next = node 
            prev = node 
            l2current = l2current.next 
        if addOne == 1:
            node = ListNode(1)
            prev.next = node             
        return before_head.next 