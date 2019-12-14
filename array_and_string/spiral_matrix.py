class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        i, j, row, col = 0, 0, len(matrix), len(matrix[0])
        res, visited, d, four_direction = [], set(), 0, [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for _ in range(row * col):
            res.append(matrix[i][j])
            visited.add((i,j))
            orignal_i, original_j = i, j
            i, j = i + four_direction[d][0], j + four_direction[d][1]
            if i >= row or j >= col or i < 0 or j < 0 or (i, j) in visited:
                # go back if hitting the boundary
                i, j, d = orignal_i, original_j, (d + 1) %4
                i, j = i + four_direction[d][0], j + four_direction[d][1]
        return res 
