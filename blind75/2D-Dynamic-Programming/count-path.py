class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize bottom rows to all 1
        row = [1] * n

        # go through all rows except the last
        for i in range(m-1):
            newRow = [1] * n
            # go through all the cols except the last
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        
        return row[0]