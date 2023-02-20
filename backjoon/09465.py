# 9465. 스티커
# Link: https://www.acmicpc.net/problem/9465
# Difficulty: Silver 1
# Category: 다이나믹 프로그래밍
from typing import List


# Solution 1: dynamic programming
# Time: 784 ms
# Memory: 49148 KB
class Solution:
    def get_answer(self, n: int, stickers: List[List[int]]) -> int:
        dp = [[0] for _ in range(3)]
        for i in range(n):
            dp[0].append(max(dp[1][i], dp[2][i]) + stickers[0][i])
            dp[1].append(max(dp[0][i], dp[2][i]) + stickers[1][i])
            dp[2].append(max(dp[0][i], dp[1][i]))
        return max(r[-1] for r in dp)


t = int(input())
for _ in range(t):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    answer = Solution().get_answer(n, stickers)
    print(answer)
