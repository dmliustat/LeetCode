"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        # write your code here
        subtreeA, subtreeD, longest = self.helper(root, 0)
        return longest;
        
    def helper(self, root, longest):
        if (root == None):
            return (0, 0, longest);
        
        leftA, leftD, longest = self.helper(root.left, longest)
        rightA, rightD, longest = self.helper(root.right, longest)
        subtreeA = 1 # A refers to the ascending tree, where root > child
        subtreeD = 1 # D refers to the descending tree, where root < child
        if ((root.left != None) & (root.right != None)):
            if ((root.val + 1 == root.left.val) & (root.val - 1 == root.right.val)):
                subtreeD = leftD + 1
                subtreeA = rightA + 1
                longest = max(leftD + rightA + 1, longest, subtreeA, subtreeD)
            if ((root.val - 1 == root.left.val) & (root.val + 1 == root.right.val)):
                subtreeD = rightD + 1
                subtreeA = leftA + 1
                longest = max(leftA + rightD + 1, longest, subtreeA, subtreeD)
        if (root.left != None):
            if (root.val + 1 == root.left.val):
                subtreeD = max(leftD + 1, subtreeD)
            if (root.val - 1 == root.left.val):
                subtreeA = max(leftA + 1, subtreeA)
        if (root.right != None):
            if (root.val + 1 == root.right.val):
                subtreeD = max(rightD + 1, subtreeD)
            if (root.val - 1 == root.right.val):
                subtreeA = max(rightA + 1, subtreeA)
        
        longest = max(subtreeA, subtreeD, longest)
        return (subtreeA, subtreeD, longest);