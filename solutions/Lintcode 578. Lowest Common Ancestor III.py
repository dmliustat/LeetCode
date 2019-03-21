class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        result = self.helper(root, A, B)
        if (result[0] and result[1]):
            return result[2];
        return None;
        
    def helper(self, node, A, B):
        # return a_exist, b_exist, ancestor
        if (node == None):
            return False, False, None
        left = self.helper(node.left, A, B)
        right = self.helper(node.right, A, B)
        A_exist = left[0] or right[0] or (A == node)
        B_exist = left[1] or right[1] or (B == node)
        if (node == A or node == B):
            return A_exist, B_exist, node;
        if (left[2] != None and right[2] != None):
            return A_exist, B_exist, node;
        if (left[2] != None):
            return A_exist, B_exist, left[2];
        if (right[2] != None):
            return A_exist, B_exist, right[2];
         
        return A_exist, B_exist, None;