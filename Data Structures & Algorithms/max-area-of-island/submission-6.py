class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def valid(i,j):
            return 0<=i<m and 0<=j<n and grid[i][j] == 1
        def bfs(i,j):
            grid[i][j] = 0
            count = 1
            q = deque()
            q.append((i,j))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while q:
                x,y = q.popleft()
                for dx,dy in directions:
                    nx,ny = x+dx,y+dy
                    if valid(nx,ny):
                        grid[nx][ny] = 0
                        q.append((nx,ny))
                        count += 1
            return count
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area,bfs(i,j))
        return max_area