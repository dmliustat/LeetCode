# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        treeSum = 0
        if (root == None):
            return False;
        if ((root.left == None) and (root.right == None)):
            treeSum += root.val
            return (treeSum == sum);
        left = False
        right = False
        if (root.left != None):
            left = self.hasPathSum(root.left, sum - root.val)
        if (root.right != None):
            right = self.hasPathSum(root.right, sum - root.val)
        return (left or right);
            