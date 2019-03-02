# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if (root == None):
            return 0;
        result = 0
        result = self.helper(root, 0, sum, result)
        
        left = self.pathSum(root.left, sum)
        right = self.pathSum(root.right, sum)
        result += left
        result += right
        return result;
    
    def helper(self, node, currSum, sum, result):
        if (node == None):
            return result;
        currSum = currSum + node.val
        if currSum == sum:
            result += 1
        result = self.helper(node.left, currSum, sum, result)
        result = self.helper(node.right, currSum, sum, result)
        return result;
        