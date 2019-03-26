class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if (root == None):
            return result;
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            result.append(list(level))
        return result;