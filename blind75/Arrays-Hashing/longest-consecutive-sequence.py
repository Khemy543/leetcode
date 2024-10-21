from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        count = 0

        for n in nums:
            # check if it is start of sequence
            if (n-1) not in hashSet:
                i = 0
                while n + i in hashSet:
                    i += 1
                count = max(count, i)
        return count

print(Solution.longestConsecutive('s', [100,4,200,1,3,2]))