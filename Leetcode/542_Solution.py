from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        move = [[1,0], [-1,0], [0,1], [0,-1]]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = m+n
        

        while q:
            i, j = q.popleft()
            for dx, dy in move:
                x = dx + i
                y = dy + j

                if 0<=x<m and 0<=y<n and mat[x][y] > mat[i][j] + 1:
                    q.append((x,y))
                    mat[x][y] = mat[i][j] + 1
        return mat
