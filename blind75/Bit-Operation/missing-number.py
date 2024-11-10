from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            n = i - nums[i]
            res += n
        return res

Solution().missingNumber([1,2,3])