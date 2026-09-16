# Multi Source BFS
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        if fresh == 0:
            return 0
        time = -1
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == 1:
                        q.append((nx,ny))
                        grid[nx][ny] = 2
                        fresh-=1
            time+=1
        if fresh == 0:
            return time
        else:
            return -1