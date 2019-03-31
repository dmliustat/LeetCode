class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if (root == None):
            return result;
        queue = [root]
        L2R = True
        while queue:            
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not L2R:
                level = reversed(level)
            L2R = not L2R
            result.append(list(level))   
        return result;