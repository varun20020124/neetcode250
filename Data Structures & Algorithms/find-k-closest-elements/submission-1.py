class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []
        for num in arr:
            diff.append((abs(num-x), num))
        heapq.heapify(diff)
        result = []
        for _ in range(k):
            dist, num = heapq.heappop(diff)
            result.append(num)
        return sorted(result)