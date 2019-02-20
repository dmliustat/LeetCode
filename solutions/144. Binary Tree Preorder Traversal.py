# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Non-recursion, 60 ms
class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        preorder = list()
        stack = list()        
        if (root is None):
            return preorder;

        while (root or stack):
            while root:
                preorder.append(root.val)
                stack.append(root)
                root = root.left

            root = stack.pop()
            root = root.right
            
        return preorder;

# Traverse, 32 ms
class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        result = list()
        def traverse(node):
            if (node is None):
                return;
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
            return;
        traverse(root)
        return result;        

# Divide & Conquer, 36 ms
class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        result = list()
        # Null or Leaf
        if ((root is None) or (not root)):
            return result;
        
        # Divide
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        # Conquer
        result.append(root.val)
        result.extend(left)
        result.extend(right)

        return result;        