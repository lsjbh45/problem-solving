# 70. Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy
# Category: Math
# Category: Dynamic Programming
# Category: Memoization


# Solution 1: dynamic programming
# Time: 32 ms
# Memory: 13.8 MB
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for _ in range(2, n + 1):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
