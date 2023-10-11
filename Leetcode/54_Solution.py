class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix:
            res += matrix.pop(0)

            for i in range(len(matrix)):
                if matrix[i]:
                    res.append(matrix[i].pop())
                    matrix[i].reverse()
            
            matrix.reverse()
        return res
