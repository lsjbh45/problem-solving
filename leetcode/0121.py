# 121. Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Category: Array
# Category: Dynamic Programming
from typing import List
import sys


# Solution 1:
# Time: 964 ms (O(n))
# Memory: 25 MB
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        local_min, local_max = prices[0], prices[0]

        for price in prices:
            if price < local_min:
                max_profit = max(max_profit, local_max - local_min)
                local_min, local_max = price, price
            else:
                if price > local_max:
                    local_max = price
        max_profit = max(max_profit, local_max - local_min)

        return max_profit


# Solution 2: current value - minimum value
# Time: 1162 ms (O(n))
# Memory: 25 MB
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
