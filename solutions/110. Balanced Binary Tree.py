# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        B, D = self.helper(root)
        return B;
    
    # 1. definition
    def helper(self, root: TreeNode):     
        # 3. exit
        if (root == None):
            return True, 0;
        
        # 2. split
        left, leftDepth = self.helper(root.left)
        right, rightDepth = self.helper(root.right)
        # subtree not balanced
        if ((left == False) or (right == False)):
            return False, -1;
        # subtrees balanced but root not balanced 
        if (abs(leftDepth - rightDepth) > 1):
            return False, -1;
        # balanced
        return True, (max(leftDepth, rightDepth) + 1);
