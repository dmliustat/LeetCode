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
    def longestConsecutive(self, root):
        # write your code here
        subtreeLongest, longest = self.helper(root, 0)
        return longest;
        
    def helper(self, root, longest):
        if (root == None):
            return (0, longest);
        
        left, longest = self.helper(root.left, longest)
        right, longest = self.helper(root.right, longest)
        
        subtreeLongest = 1 # at least there is root
        if (root.left != None):
            if (root.val + 1) == root.left.val:
                subtreeLongest = max(subtreeLongest, (left + 1))
        if (root.right != None):
            if (root.val + 1) == root.right.val:
                subtreeLongest = max(subtreeLongest, (right + 1))
        if (subtreeLongest > longest):
            longest = subtreeLongest
            
        return (subtreeLongest, longest);
