# Duplicate Integer
# Given an integer array nums, return true if any value 
# appears more than once in the array, otherwise return false.

# Input: nums = [1, 2, 3, 3]

# Output: true

# Input: nums = [1, 2, 3, 4]

# Output: false

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

Solution().hasDuplicate([1, 2, 3, 3])