class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val;
            root = root.right