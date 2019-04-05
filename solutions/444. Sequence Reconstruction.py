class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        # edge map
        Map = {}
        for seq in seqs:
            for node in seq:
                if node not in Map:
                    Map[node] = set()
        
        for seq in seqs:
            for i in range(len(seq)-1):
                Map[seq[i]].add(seq[i+1])
        
        # get indegrees  
        indegree = {node: 0 for node in Map}
        for node in Map:
            for nb in Map[node]:
                indegree[nb] += 1
                
        # topological sorting 
        queue = []
        order = []
        for node in Map:
            if indegree[node] == 0:
                queue.append(node)
            
        while queue:
            if len(queue) > 1:
                return False;
            node = queue.pop(0)
            order.append(node)
            for nb in Map[node]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    queue.append(nb)
              
        return order == org;
        
    