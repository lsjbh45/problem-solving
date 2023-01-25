# 122. Best Time to Buy and Sell Stock II
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Difficulty: Medium
# Category: Array
# Category: Dynamic Programming
# Category: Greedy
from typing import List


# Solution 1: greedy algorithm
# Time: 151 ms
# Memory: 15.1 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit
