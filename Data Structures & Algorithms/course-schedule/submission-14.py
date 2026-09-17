from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def topological():
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
            return len(result) == numCourses
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
        return topological()
        