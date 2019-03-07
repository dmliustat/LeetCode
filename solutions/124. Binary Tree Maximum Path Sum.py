# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxPath, _ = self.helper(root)
        return maxPath;
    
    def helper(self, node):
        if (node == None):
            return -sys.maxsize - 1, 0;
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        maxPath = max(left[0], right[0], left[1] + right[1] + node.val)
        singlePath = max(left[1] + node.val, right[1] + node.val, 0)
        return maxPath, singlePath