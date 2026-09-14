import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = []
        for task, freq in count.items():
            heapq.heappush(maxheap, (-freq,task))
        cooldown = deque()
        time = 0
        while maxheap or cooldown:
            time+=1
            if maxheap:
                freq, task = heapq.heappop(maxheap)
                freq+=1
                if freq < 0:
                    cooldown.append((time+n, freq, task))
            if cooldown and cooldown[0][0] == time:
                _, freq, task = cooldown.popleft()
                heapq.heappush(maxheap, (freq, task))
        return time