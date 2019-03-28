class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if (root == None):
            return "{}";
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] != None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)            
            index += 1
        while queue[-1] == None:
            queue.pop()
        
        return "{%s}" % ','.join([str(node.val) if node is not None else '#' for node in queue]);
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('\n')
        if data == '{}':
            return None;
        
        nodes = data[1:-1].split(',')
        root = TreeNode(int(nodes[0]))
        queue = [root]
        isLeftNode = True
        index = 0
        for n in nodes[1:]:
            if n != '#':
                node = TreeNode(int(n))
                if isLeftNode:
                    queue[index].left = node
                else:
                    queue[index].right = node                   
                queue.append(node)
            
            if not isLeftNode:
                index += 1
            isLeftNode = not isLeftNode
            
        return root;