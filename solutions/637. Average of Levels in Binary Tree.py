class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = self.helper(root, [], 0)
        return [sum(subTree)/len(subTree) for subTree in result];
        
    def helper(self, node: TreeNode, result: List[List[int]], level):
        if (node == None):
            return;
        if (level == 0):
            result = [[node.val]]
        elif (level < len(result)):
            result[level].append(node.val)
        else:
            result.append([node.val])
        self.helper(node.left, result, level + 1)
        self.helper(node.right, result, level + 1)
        return result;