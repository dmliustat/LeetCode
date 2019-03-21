class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        self.subtreeAve = -sys.maxsize - 1
        self.maxSubtree = root
        self.helper(root, self.subtreeAve, self.maxSubtree)
        return self.maxSubtree;
        
    def helper(self, node, subtreeAve, maxSubtree):
        # return treeSum, size
        if (node == None):
            return 0, 0;
        
        left = self.helper(node.left, self.subtreeAve, self.maxSubtree)
        right = self.helper(node.right, self.subtreeAve, self.maxSubtree)
        
        Sum = left[0] + right[0] + node.val
        if Sum > self.subtreeAve * (left[1] + right[1] + 1):
            self.subtreeAve = Sum * 1.0/(left[1] + right[1] + 1)
            self.maxSubtree = node
            
        return Sum, left[1] + right[1] + 1;