import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        minheap = [(0, k)]
        visited = set()
        time = 0
        while minheap:
            dist, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            time = dist
            for adj,weight in graph[node]:
                if adj not in visited:
                    heapq.heappush(minheap, (dist + weight, adj))
        if n == len(visited):
            return time
        return -1