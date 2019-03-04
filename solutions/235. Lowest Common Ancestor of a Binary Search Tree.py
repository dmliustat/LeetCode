# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q);
        
    def helper(self, node, p, q):
        if (node == p or node == q or node == None):
            return node;
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)
        
        if (left != None and right != None):
            return node;
        if (left == None):
            return right;
        if (right == None):
            return left;
        