from typing import List


class Solution:
    def TallCout(self, heights: List[int]) -> int:
        count = 1

        for i in range(len(heights)):
            if (i-1) >= 0 and heights[i] > heights[i-1]:
                count += 1
            
        return count
    

print(Solution().TallCout([1, 2, 3, 4, 5]))
