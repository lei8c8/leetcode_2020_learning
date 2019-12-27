from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = [defaultdict(int) for i in range(9)]
        col_map = [defaultdict(int) for i in range(9)]
        box_map = [defaultdict(int) for i in range(9)]
        for i in range(9):
            for j in range(9):
                box_id = (i // 3) * 3 + (j // 3)
                if board[i][j] != '.':
                    row_map[i][board[i][j]] += 1
                    col_map[j][board[i][j]] += 1
                    box_map[box_id][board[i][j]] += 1
                if row_map[i][board[i][j]] > 1 or col_map[j][board[i][j]] > 1 or box_map[box_id][board[i][j]] > 1:
                    return False 
        return True
