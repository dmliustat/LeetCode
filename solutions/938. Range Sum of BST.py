class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.result = 0
        self.helper(root, L, R, self.result)
        return self.result;
    
    def helper(self, node, L, R, result):
        if node == None:
            return;
        if node.val < L:
            self.helper(node.right, L, R, result)
        elif node.val > R:
            self.helper(node.left, L, R, result)
        else:
            self.result += node.val
            self.helper(node.left, L, R, result)
            self.helper(node.right, L, R, result)