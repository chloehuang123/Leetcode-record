from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        m = len(grid)
        n = len(grid[0])
        move = [[1,0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        fresh_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_count += 1

        
        if fresh_count == 0:
            return 0
        
        res = 0
        while q:
            if fresh_count == 0:
                return res
            res += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in move:
                    x = dx + i
                    y = dy + j

                    if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh_count -= 1
                        q.append((x, y))
    
        return -1
            
