from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the input
        nums.sort()

        for i, value in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L, R = i + 1,  len(nums) -1
            while L < R:
                threeSum = nums[i] + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                if threeSum < 0:
                    L += 1
                if(threeSum == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L -1] and L < R:
                        L += 1
        return res 