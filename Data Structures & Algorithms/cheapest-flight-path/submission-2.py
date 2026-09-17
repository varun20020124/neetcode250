import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,price in flights:
            graph[u].append((v,price))
        minheap = [(0,src,0)] # cost, node, edges_used
        best_edges = [math.inf] * n
        while minheap:
            cost, node, edges_used = heapq.heappop(minheap)
            if node == dst:
                return cost
            if edges_used >= best_edges[node]:
                continue
            best_edges[node] = edges_used

            if edges_used == k + 1:
                continue
            for adj,price in graph[node]:
                heapq.heappush(minheap,(cost+price, adj, edges_used+1))
        return -1