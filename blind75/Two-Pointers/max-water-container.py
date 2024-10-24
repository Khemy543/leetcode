from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        myMaxArea = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            width = R - L
            area = min(heights[L], heights[R]) * width
            
            if area > myMaxArea:
                myMaxArea = area
            
            if heights[L] > heights[R]:
                R = R - 1
            else:
                L = L + 1
        return myMaxArea