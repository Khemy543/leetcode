from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r,c) in path):
                return False
            path.add((r,c))

            for dr, dc in directions:
                result = dfs (dr+r, dc+c, i+1)
                if result == True:
                    return True
                    break
            path.remove((r,c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False

# big O notation = O(m * n * 4^n)