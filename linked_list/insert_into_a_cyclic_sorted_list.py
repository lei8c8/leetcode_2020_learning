class Solution:
    def insert(self, head, insertVal):
        if head is None:
            node = ListNode(insertVal)
            node.next = node 
            return node 
        left, right, insert = head, head.next, False
        while True:
            if left.val <= insertVal <= right.val:
                insert = True 
            if left.val > right.val:
                if left.val <= insertVal or right.val >= insertVal:
                    insert = True 
            if insert:
                node = ListNode(insertVal)
                left.next = node 
                node.next = right 
                return head 
            left, right = right, right.next 
            if left == head:
                break 
        node = ListNode(insertVal)
        left.next = node 
        node.next = right 
        return head 


            

