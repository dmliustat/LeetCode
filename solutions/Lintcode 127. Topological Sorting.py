class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        orders = []
        if (graph == None):
            return orders;
            
        # 1. count indegree
        indegree = {}
        for node in graph:
            indegree[node] = 0
        for node in graph:
            for nb in node.neighbors:
                indegree[nb] += 1
                
        # 2. topological sorting, BFS
        queue = []
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)
                orders.append(node)
                
        while queue:
            node = queue.pop(0)
            for nb in node.neighbors:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    queue.append(nb)
                    orders.append(nb)
                    
        return orders;