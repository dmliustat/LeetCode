class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if (p == None):
            return p;
        if (p.right != None):
            return self.getMin(p.right);
        
        # p.right == None
        succ = None    
        while root != None:
            if p.val < root.val:
                succ = root
                root = root.left
            if p.val >= root.val:
                root = root.right
        return succ;
        
        
    def getMin(self, node):
        while node.left != None:
            node = node.left
        return node;