# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorder_helper(root, res)
        return res 
    
    def preorder_helper(self, root, res):
        if not root:
            return 
        res.append(root.val)
        self.preorder_helper(root.left, res)
        self.preorder_helper(root.right, res)