# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if (root == None):
            return [];
        paths = []
        self.helper(root, [], paths, sum)
        return paths;
    
    def helper(self, node, currPath, paths, target):
        if ((node.left == None) and (node.right == None)):
            currPath.append(node.val)
            if sum(currPath) == target:
                paths.append(currPath)
            return;
        if (node.left != None):
            path = currPath + [node.val]
            self.helper(node.left, path, paths, target)
        if (node.right != None):
            path = currPath + [node.val]
            self.helper(node.right, path, paths, target)
        