class Solution:
    def hasCycle(self, head):
        if not head or not head.next or not head.next.next:
            return False
        slow, fast = head, head.next
        while True:
            try:
                fast = fast.next.next 
                slow = slow.next 
            except:
                return False 
            if slow == fast:
                return True