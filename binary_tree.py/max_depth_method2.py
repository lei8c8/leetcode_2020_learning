class Solution:
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.inorder(root, 1)
        return self.depth  

    def inorder(self, root, depth):
        if not root:
            return 0
        if not root.left and not root.right:
            self.depth = max(self.depth, depth)
        self.inorder(root.left, depth + 1)
        self.inorder(root.right, depth + 1)