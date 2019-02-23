# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Traverse
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if ((root == None) or (not root)):
            return [];
        result = []                    
        self.helper(root, str(root.val), result)
        return result;
    
    def helper(self, node, currPath, result):
        if ((node.left == None) & (node.right == None)):
            result.append(currPath)
            return;
        if (node.left != None):
            path = currPath + "->" + str(node.left.val)
            self.helper(node.left, path, result)
        if (node.right != None):
            path = currPath + "->" + str(node.right.val)
            self.helper(node.right, path, result)
    