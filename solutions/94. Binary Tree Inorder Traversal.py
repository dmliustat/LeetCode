# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if (root == None):
            return [];
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right);

class Solution:    
    def inorderTraversal(self, root):
        if root is None:
            return [];
        
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
            
        inorder = []
        
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)
                
        return inorder;   