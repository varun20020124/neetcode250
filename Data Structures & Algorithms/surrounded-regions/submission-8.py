from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        q = deque()
        seen = set()
        for i in range(m):
            for j in range(n):
                if i == 0 and board[i][j] == "O" and (i,j) not in seen:
                    q.append((i,j))
                    seen.add((i,j))
                if j == 0 and board[i][j] == "O" and (i,j) not in seen:
                    q.append((i,j))
                    seen.add((i,j))
                if j == len(board[0])-1 and board[i][j] == "O" and (i,j) not in seen:
                    q.append((i,j))
                    seen.add((i,j))
                if i == len(board)-1 and board[i][j] == "O" and (i,j) not in seen:
                    q.append((i,j))
                    seen.add((i,j))
        while q:
            x,y = q.popleft()
            board[x][y] = "#"
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and board[nx][ny] == "O":
                    q.append((nx,ny))
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
