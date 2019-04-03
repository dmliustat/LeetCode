class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        orders = []

        # 1. collect indegree (list) and edges (dictionary)
        edgeMap = {i: [] for i in range(numCourses)}
        indegree = [0 for i in range(numCourses)]

        for pair in prerequisites:
            edgeMap[pair[1]].append(pair[0])
            indegree[pair[0]] += 1
        # print(indegree)    

        # 2. topological sorting -- BFS
        queue = []
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
                orders.append(course)
        while queue:
            course = queue.pop(0)
            for precourse in edgeMap[course]:
                indegree[precourse] -= 1
                if indegree[precourse] == 0:
                    queue.append(precourse)
                    orders.append(precourse)
        if len(orders) != numCourses:
            return [];
        return orders;