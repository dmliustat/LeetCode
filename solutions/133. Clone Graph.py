class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node;
        root = node
        # Use BFS to traverse all nodes in the graph
        nodes = self.getNodes(node)
        
        edgeMap = {}
        for node in nodes:
            edgeMap[node] = Node(node.val, [])
        for node in nodes:
            node_new = edgeMap[node]
            for nb in node.neighbors:
                nb_new = edgeMap[nb]
                node_new.neighbors.append(nb_new)
        return edgeMap[root];
   

    def getNodes(self, node):
        queue = [node]
        result = set([node])
        while queue:
            head = queue.pop(0)
            for nb in head.neighbors:
                if nb not in result:
                    result.add(nb)
                    queue.append(nb)
        return result;