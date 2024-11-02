from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max((nums[i] + dfs(i+2)), dfs(i+1))
            return cache[i]
        
        return dfs(0)
    
    def robBottomUp(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
           temp = max(n + rob1, rob2)
           rob1 = rob2
           rob2 = temp
        return rob2
    
