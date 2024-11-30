from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        print(nums[-1])

        while L <= R:
            mid = (L+R)//2

            if target == nums[mid]:
                return mid
            
            if nums[L] <= nums[mid]:
                if target > nums[mid] or target < nums[L]:
                    L = mid + 1
                else:
                    R = mid - 1
            
            else:
                if target < nums[mid] or target > nums[R]:
                    R = mid - 1
                else:
                    L = mid + 1
        return -1
    

print(Solution().search([1,2,3,4,5,6], 3))