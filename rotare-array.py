from typing import List


class Solution:
    def rotate(self, nums: List[int], k:int) -> None:
        
        # solution 1
        k = k % len(nums)

        def reverse(l,r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l,r = l+1, r-1
        
        reverse(0, len(nums) -1)
        reverse(0, k-1)
        reverse(k, len(nums) -1)

        # solution 2
        i = k
        while i<=k:
            last = nums.pop()
            nums.insert(0, last)
            i += 1


        # solution 3
        rotatedNums = []

        for i in range(len(nums)):
            index = (i+k) % len(nums)
            rotatedNums[index] = nums[i]
            return rotatedNums
