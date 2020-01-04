class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder_helper(root, res)
        return res
        
    def inorder_helper(self, root, res):
        if not root: 
            return None 
        self.inorder_helper(root.left, res)
        res.append(root.val)
        self.inorder_helper(root.right, res)