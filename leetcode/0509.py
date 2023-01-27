# 509. Fibonacci Number
# Link: https://leetcode.com/problems/fibonacci-number/
# Difficulty: Easy
# Category: Math
# Category: Dynamic Programming
# Category: Recursion
# Category: Memoization


# Solution 1: Memoization
# Time: 35 ms
# Memory: 13.8 MB
class Solution1:
    dp = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if n not in self.dp:
            self.dp[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.dp[n]


# Solution 2: Tabulation
# Time: 34 ms
# Memory: 13.9 MB
class Solution2:
    def fib(self, n: int) -> int:
        dp = [0, 1]

        for _ in range(2, n + 1):
            dp.append(dp[-1] + dp[-2])

        return dp[n]
