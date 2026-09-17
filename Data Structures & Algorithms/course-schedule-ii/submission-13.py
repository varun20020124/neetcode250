from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def topological(graph):
            q = deque()
            indegree = [0] * numCourses
            for i in range(numCourses):
                for j in graph[i]:
                    indegree[j]+=1
            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)
            result = []
            while q:
                node = q.popleft()
                result.append(node)
                for adj in graph[node]:
                    indegree[adj]-=1
                    if indegree[adj] == 0:
                        q.append(adj)
            return result
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
        result = topological(graph)
        if len(result) == numCourses:
            return result
        else:
            return []
        