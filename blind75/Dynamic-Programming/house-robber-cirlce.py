from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
            
        def dfs(i, arr, cache):
            if i >= len(arr):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(arr[i] + dfs(i + 2, arr, cache), dfs(i + 1, arr, cache))
            return cache[i]
        
        # report house robber 1
        def helper(arr):
            cache = [-1] * len(arr)
            return dfs(0, arr, cache)
        
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))
    
