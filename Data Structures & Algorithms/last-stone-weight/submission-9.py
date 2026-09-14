class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        maxheap = stones
        heapq.heapify(maxheap)
        while len(maxheap) >= 2:
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)
            if x!=y:
                heapq.heappush(maxheap, x-y)
        if maxheap:
            return -heapq.heappop(maxheap)
        else:
            return 0