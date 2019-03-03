# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if (root == None):
            return 0;  
        return self.helper(root, 0)[1];
        
    def helper(self, node, tilt):
        if (node == None):
            return (0, tilt);
        
        left = self.helper(node.left, tilt)
        right = self.helper(node.right, tilt)
        
        tilt = abs(left[0] - right[0]) + left[1] + right[1]

        return (left[0]+right[0]+node.val, tilt);