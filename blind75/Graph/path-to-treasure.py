from typing import List

class Solution:
    def findTreasure(self, map: List[List[int]]) -> int:
        rows, cols = len(map), len(map[0])
        visited = set()
        queue = []
        results = []

        directions = [(0,1), (1,0), (-1,0),(0,-1)]

        visited.add((0,0))
        queue.append((0,0))
        results.append((0,0))

        while queue:
            row, col = queue.pop(0)

            if map[row][col] == 1:
                return results

            for dr, dc in directions:
                r,c = row + dr, col + dc
                
                if r >= 0 and r < rows and c >= 0 and c < cols and (r,c) not in visited:
                    if map[r][c] == 0 or map[r][c] == 1:
                        visited.add((r,c))
                        queue.append((r,c))
                        results.append((r,c))
        return []

map_grid = [
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
print(Solution().findTreasure(map_grid))                