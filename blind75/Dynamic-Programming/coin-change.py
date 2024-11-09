from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # example: coins: [1,3,4,5], amount: 7
        # dp[0] = 0, dp[1] = 1 + dp[0]... dp[7] = 1 + dp[6]
        
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != float('inf') else -1