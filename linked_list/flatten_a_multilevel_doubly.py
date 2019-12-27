class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        stack, cur = [], head
        while cur or stack:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                node = cur.child
                cur.next = node
                node.prev = cur
                cur.child = None
                cur = node
            elif not cur.next and len(stack) > 0:
                node = stack.pop()
                cur.next = node
                node.prev = cur
                cur = node 
            else:
                cur = cur.next
        return head       