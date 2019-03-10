class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if (root == None):
            return TreeNode(val);
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root;