class Solution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        oddHead, evenHead = head, head.next
        oddCurrent, evenCurrent = oddHead, evenHead
        while oddCurrent.next.next and evenCurrent.next.next:
            oddCurrent.next = oddCurrent.next.next
            evenCurrent.next = evenCurrent.next.next 
            oddCurrent = oddCurrent.next 
            evenCurrent = evenCurrent.next     
        if evenCurrent.next:
            oddCurrent.next = evenCurrent.next 
            oddCurrent = oddCurrent.next
            evenCurrent.next = None 
        oddCurrent.next = evenHead
        return oddHead

        