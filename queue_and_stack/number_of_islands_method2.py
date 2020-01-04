class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        row_num, col_num = len(grid), len(grid[0])
        ans = 0
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    ans += 1
        return ans

    def dfs(self, grid, r, c):
        row_num, col_num = len(grid), len(grid[0])
        if (r < 0 or r >= row_num or c < 0 or c >= col_num or grid[r][c] == '0'):
            return 
        grid[r][c] = '0'
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)
