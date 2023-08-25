class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                grid[x][y] = '0'
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)
        
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res

"""
像病毒式扩散
"""
