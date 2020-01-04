from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row_num = len(matrix)
        col_num = len(matrix[0]) if row_num else 0
        for i in range(row_num):
            for j in range(col_num):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')
                    up_min = matrix[i-1][j] + 1 if i > 0 else matrix[i][j]
                    left_min = matrix[i][j-1] + 1 if j > 0 else matrix[i][j]
                    matrix[i][j] = min(up_min, left_min, matrix[i][j])
        for i in range(row_num - 1, -1, -1):
            for j in range(col_num - 1, -1, -1):
                if matrix[i][j] != 0:
                    down_min = matrix[i+1][j] + 1 if i < row_num -1 else matrix[i][j]
                    right_min = matrix[i][j+1]  + 1 if j < col_num - 1 else matrix[i][j]
                    matrix[i][j] = min(down_min, right_min, matrix[i][j])
        return matrix