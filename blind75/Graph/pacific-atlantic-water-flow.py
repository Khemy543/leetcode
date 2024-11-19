from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r,c, visit, prevHeight):
            # check if value is not visted is bounded and is less than the previous height
            if((r,c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for col in range(cols):
            # get all columns that touch the pacific ocean 
            dfs(0, col, pacific, heights[0][col])
            # get all columns that touch atlantic ocean
            dfs(rows - 1, col, atlantic, heights[rows-1][col])

        for row in range(rows):
            # get all rows that touch the pacific ocean 
            dfs(row, 0, pacific, heights[row][0])
            # get all rows that touch the atlantic ocean 
            dfs(row, cols - 1, atlantic, heights[row][cols-1])
        
        # find common values of the pacific and atlantic ocean
        commonValues = pacific & atlantic
        # return a list of lists
        return [list(item) for item in commonValues]