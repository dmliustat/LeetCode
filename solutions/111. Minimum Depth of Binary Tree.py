# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        if ((root == None) or (not root)):
            return 0;
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if ((left == 0) & (right == 0)):
            return 1;
        elif (left == 0):
            return (right + 1);
        elif (right == 0):
            return (left + 1);
        else:
            return (min(left, right) + 1);