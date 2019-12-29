from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    answer += 1
        return answer
        
    def bfs(self, grid, i, j):
        directions = [(i,j+1),(i,j-1),(i-1,j),(i+1,j)]
        q = deque()
        for x, y in directions:
            q.append((x, y))
        while q:
            d1, d2 = q.popleft()
            if 0 <= d1 < len(grid) and 0 <= d2 < len(grid[0]) and grid[d1][d2] == '1':
                grid[d1][d2] = '0'
                dirs = [(d1,d2+1),(d1,d2-1),(d1-1,d2),(d1+1,d2)]
                for x1, y1 in dirs:
                        q.append((x1,y1))
