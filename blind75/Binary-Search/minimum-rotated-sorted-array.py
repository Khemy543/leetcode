from typing import List

class Solution:
    """ def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        lowest = float('infinity')

        while nums[L] > nums[R]:
            mid = round((L+R)/2)
            lowest = min(nums[L], nums[mid], lowest)

            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid - 1
        lowest = min(lowest, nums[L])

        return lowest """
    
    def findMin(self, nums: List[int]) -> int:
        lowest = nums[0]
        L, R = 0, len(nums) -1 

        while L <= R:
            if nums[L] < nums[R]:
                lowest = min(lowest, nums[L])
                break
            mid = (L+R) // 2
            lowest = min(lowest, nums[mid])
            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid -1
        return lowest