class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.postorder_helper(root, res)
        return res 

    def postorder_helper(self, root, res):
        if not root:
            return 
        self.postorder_helper(root.left, res)
        self.postorder_helper(root.right, res)
        res.append(root.val)