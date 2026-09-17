from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def bfs(u,v):
            graph[u].remove(v)
            graph[v].remove(u)
            q = deque()
            q.append(u)
            visited = set()
            visited.add(u)
            while q:
                node = q.popleft()
                for adj in graph[node]:
                    if adj not in visited:
                        q.append(adj)
                        visited.add(adj)
            graph[u].append(v)
            graph[v].append(u)
            return len(visited) == len(edges)
        for (u,v) in reversed(edges):
            if bfs(u,v):
                return [u,v]