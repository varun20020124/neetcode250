from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                components+=1
                bfs(visited,i)
        return components