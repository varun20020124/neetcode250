class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Of all cells currently reachable from my explored region, which has the lowest elevation?
        minheap = [(grid[0][0], 0, 0)]
        visited = set()
        time = 0
        while minheap:
            elevation, x,y = heapq.heappop(minheap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            time = max(time, elevation)
            if x == len(grid)-1 and y == len(grid[0])-1:
                return time
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and (nx,ny) not in visited:
                    heapq.heappush(minheap, (grid[nx][ny],nx,ny)) # lowest possible elevation through minheap