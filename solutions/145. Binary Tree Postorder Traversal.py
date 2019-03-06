# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.postorder = []
        self.traversal(root)
        return self.postorder;
        
    def traversal(self, node):
        if (node == None):
            return;
        self.traversal(node.left)
        self.traversal(node.right)
        self.postorder.append(node.val)

    
    
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if (root == None):
            return [];
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]