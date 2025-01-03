from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            profit = max(profit, price - lowest)
        return profit