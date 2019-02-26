# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Divide and Conquer
        self.helper(root)
        
    # flatten the tree and return the last node    
    def helper(self, root):
        if (root == None):
            return None;
        leftLast = self.helper(root.left)
        rightLast = self.helper(root.right)
        
        # Connect leftLast to root.right
        if (leftLast != None):
            leftLast.right = root.right
            root.right = root.left
            root.left = None
        if (rightLast != None):
            return rightLast;
        if (leftLast != None):
            return leftLast;
        return root;
        