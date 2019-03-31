class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if (len(edges) != n-1 or n == 0):
            return False;
        edgeDict = {}
        for edge in edges:
            edgeDict[edge[0]] = edgeDict.get(edge[0], []) + [edge[1]]
            edgeDict[edge[1]] = edgeDict.get(edge[1], []) + [edge[0]]
        queue = [0]
        visited = set([0])
        while queue:
            node = queue.pop(0)
            for i in edgeDict.get(node, []):
                if i in visited:
                    continue
                queue.append(i)
                visited.add(i)
        return len(visited) == n;