from collections import deque
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def bfs(visited,src):
            visited.add(src)
            q = deque()
            q.append(src)
            while q:
                node = q.popleft()
                for adj in graph[node]:
                    if adj not in visited:
                        visited.add(adj)
                        q.append(adj)
        components = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                bfs(visited, i)
                components+=1
        return components == 1 and len(edges)==n-1