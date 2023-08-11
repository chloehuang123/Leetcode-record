class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[mid][len(matrix[mid]) - 1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                low, high = 0, len(matrix[mid]) - 1
                while low <= high:
                    matrix_mid = (low + high) // 2
                    if target == matrix[mid][matrix_mid]:
                        return True
                    elif target < matrix[mid][matrix_mid]:
                        high = matrix_mid - 1
                    else:
                        low = matrix_mid + 1
                break
        return False
