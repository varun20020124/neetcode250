class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = [(0,(points[0][0], points[0][1]))]
        def distance(point1, point2):
            x,y = point1
            a,b = point2
            return abs(x-a)+abs(y-b)
        cost = 0
        visited = set()
        while minheap and len(visited) < len(points):
            c, (x, y) = heapq.heappop(minheap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            cost+=c
            for (a,b) in points:
                if (a,b) not in visited:
                    dist = distance((a,b),(x,y))
                    heapq.heappush(minheap, (dist, (a,b)))
        return cost