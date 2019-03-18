class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return;    
        if key == root.val:
            if root.right == None:
                return root.left;
            node = root.right
            while node.left != None:
                node = node.left
            root.val, node.val = node.val, root.val # swap values
            root.right = self.deleteNode(root.right, key) # recursively delete
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root;