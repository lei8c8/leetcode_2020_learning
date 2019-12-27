class Solution:
    def removeElements(self, head, val):
        if not head: return head 
        pre, cur = None, head 
        while cur:
            if cur.val == val and cur is head:
                head = head.next 
                cur = head
            elif cur.val == val:
                pre.next = cur.next 
                cur = cur.next 
            else:
                pre = cur
                cur = cur.next 
        return head 
        