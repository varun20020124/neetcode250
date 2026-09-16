from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q_a = deque()
        q_p = deque()
        set_a = set()
        set_p = set()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    q_p.append((i,j))
                    set_p.add((i,j))
                if i == len(heights)-1 or j == len(heights[0])-1:
                    q_a.append((i,j))
                    set_a.add((i,j))
        
        def bfs(queue,set_q):
            while queue:
                x,y = queue.popleft()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<len(heights) and 0<=ny<len(heights[0]) and (nx,ny) not in set_q and heights[nx][ny] >= heights[x][y]:
                        queue.append((nx,ny))
                        set_q.add((nx,ny))
            return set_q

        return list(bfs(q_a, set_a).intersection(bfs(q_p, set_p)))