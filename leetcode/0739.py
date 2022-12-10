# 739. Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium
# Category: Array
# Category: Stack
# Category: Monotonic Stack
from typing import List


# Solution 1: stack
# Time: 3872 ms
# Memory: 28.9 MB
class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0 for _ in range(len(temperatures))]
        stack = []

        for idx, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                prev, _ = stack.pop()
                days[prev] = idx - prev
            stack.append((idx, temperature))
        return days
