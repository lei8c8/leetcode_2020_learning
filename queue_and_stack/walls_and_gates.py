from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j)
        
    def bfs(self, rooms, i, j):
        directions = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
        queue = deque()
        for x, y in directions:
            queue.append((x, y, 1))
        while len(queue) > 0:
            d_row, d_col, steps = queue.popleft()
            if 0 <= d_row < len(rooms) and 0 <= d_col < len(rooms[0]) and rooms[d_row][d_col] > steps:
                rooms[d_row][d_col] = steps
                d = [(d_row, d_col+1), (d_row, d_col-1), (d_row+1, d_col), (d_row-1, d_col)]
                for x, y in d:
                    queue.append((x, y, steps+1))



