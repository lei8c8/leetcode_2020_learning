class Solution:
    def isPalindrome(self, head):
        if not head:
            return True 
        first_half_end = self.find_end_of_first_half(head)
        second_half_start = first_half_end.next 
        reversed_second_half = self.reverse_list(second_half_start)
        res = True 
        current, another_current = head, reversed_second_half
        while another_current:
            if current.val != another_current.val:
                return False 
            current = current.next 
            another_current = another_current.next
        return res
                     
    def find_end_of_first_half(self, node):
        s, f = node, node 
        while f.next and f.next.next:
            s, f = s.next, f.next.next
        return s 

    def reverse_list(self, head):
        if not head: return head
        current, node = head, None
        while current.next:
            node = current.next 
            current.next = current.next.next
            node.next = head 
            head = node 
        return head 
        