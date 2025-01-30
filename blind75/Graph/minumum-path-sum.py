from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = [[float('inf')] * (COLS + 1) for r in range(ROWS + 1)]
        res[ROWS-1][COLS] = 0

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
        return res[0][0]
            
