# 12865. 평범한 배낭
# Link: https://www.acmicpc.net/problem/12865
# Difficulty: Gold 5
# Category: 다이나믹 프로그래밍
# Category: 배낭 문제
from typing import List, Tuple


# Solution 1: dynamic programming
# Time: 2300 ms
# Memory: 43968 KB
class Solution:
    def get_answer(self, n: int, k: int, obj: List[Tuple[int, int]]) -> int:
        dp = [0 for _ in range(k + 1)]
        for w, v in obj:
            new = []
            for i in range(k + 1):
                if i < w:
                    new.append(dp[i])
                else:
                    new.append(max(dp[i], dp[i - w] + v))
            dp = new

        return dp[-1]


n, k = map(int, input().split())
obj = [tuple(map(int, input().split())) for _ in range(n)]
answer = Solution().get_answer(n, k, obj)
print(answer)
