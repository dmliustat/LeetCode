# Traverse
class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if ((root == None) or (not root)):
            return 0;
        depth = 1
        
        def helper(node, currDepth):
            if (node == None):
                return;
            
            nonlocal depth
            if (currDepth > depth):
                depth = currDepth
            helper(node.left, currDepth + 1)
            helper(node.right, currDepth + 1)
        
        helper(root, 1)
        
        return depth;

# Divide and Conquer
class Solution:
    depth = 1    
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if ((root == None) or (not root)):
            return 0;

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left > right:
            return (left + 1);
        else:
            return (right + 1);