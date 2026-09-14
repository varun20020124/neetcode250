import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x,y in points:
            heapq.heappush(minheap, (x**2 + y**2,(x,y)))
        result = []
        for _ in range(k):
            dist,coord = heapq.heappop(minheap)
            result.append([coord[0],coord[1]])
        return result