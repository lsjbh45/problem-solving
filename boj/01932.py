# 1932. 정수 삼각형
# Link: https://www.acmicpc.net/problem/1932
# Difficulty: Silver 1
# Category: 다이나믹 프로그래밍
from typing import List


# Solution 1: dynamic programming
# Time: 220 ms
# Memory: 46008 KB
class Solution:
    def get_answer(self, n: int, triangle: List[List[int]]) -> int:
        dp = [[] for _ in range(n)] + [[0 for _ in range(n + 1)]]
        for i in range(n - 1, -1, -1):
            dp[i] = [
                triangle[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])
                for j in range(i + 1)
            ]
        return dp[0][0]


n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
answer = Solution().get_answer(n, triangle)
print(answer)
