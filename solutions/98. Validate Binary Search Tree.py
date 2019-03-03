# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if (root == None):
            return True;
        result = self.validBST(root)
        return result[0];
    
    def validBST(self, node): 
    # return isValid, subtree minimum, subtree maximum
        if (node.left == None and node.right == None):
            return (True, node.val, node.val);
        if (node.left != None and node.right != None):
            left = self.validBST(node.left)
            right = self.validBST(node.right)
            return ((left[0] & right[0] & (left[2] < node.val) & (node.val < right[1])), min(left[1], right[1], node.val), max(left[2], right[2], node.val))
        if (node.right != None):
            right = self.validBST(node.right)
            return ((right[0] & (node.val < right[1])), node.val, right[2])
        if (node.left != None):
            left = self.validBST(node.left)
            return ((left[0] & (left[2] < node.val)), left[1], node.val)