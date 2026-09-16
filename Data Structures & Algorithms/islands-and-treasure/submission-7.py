from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        INF = 2147483647
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in directions:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == INF:
                        q.append((nx,ny))
                        grid[nx][ny] = grid[x][y]+1