class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []       
        while root!= None:
            self.stack.append(root)
            root = root.left

#     def next(self) -> int:
#         """
#         @return the next smallest number
#         """
#         node = self.stack[-1]
#         if node.right != None:
#             temp = node.right
#             while temp != None:
#                 self.stack.append(temp)
#                 temp = temp.left
#         else:
#             temp = self.stack.pop()
#             while self.stack and self.stack[-1].right == temp:
#                 temp = self.stack.pop()        
        
#         return node.val;
        
    def next(self):
        node = self.stack.pop()
        temp = node.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0;