class Solution:
    def climbStairsUsingCache(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                return int(i == n)
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0)
    
    def climbingStairsUsingSpaceOptimization(self, n:int) -> int:
        left, right = 1, 1

        for i in range(n-1):
            temp = left
            left = left + right
            right = temp
        
        return left


print(Solution().climbStairsUsingCache(5))
print(Solution().climbingStairsUsingSpaceOptimization(5))