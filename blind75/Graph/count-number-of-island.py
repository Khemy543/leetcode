from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()

                # our frontiers will be the values in next to current
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # left, up, right, down

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if(r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                        visited.add((r, c))
                        queue.append((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands



grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]