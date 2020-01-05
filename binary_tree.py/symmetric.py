# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = deque([(root.left, root.right)])
        while q:
            l, r = q.popleft()
            if not l and not r:
                continue
            if (not l or not r) or l.val != r.val:
                return False 
            q.append((l.left, r.right))
            q.append((l.right, r.left))
        return True 

        