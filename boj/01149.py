# 1149. RGB거리
# Link: https://www.acmicpc.net/problem/1149
# Difficulty: Silver 1
# Category: 다이나믹 프로그래밍
from typing import List, Tuple


# Solution 1: dynamic programming
# Time: 176 ms
# Memory: 38848 KB
class Solution:
    def get_answer(self, n: int, cost: List[List[int]]):
        acc: List[Tuple[int, int, int]] = [(0, 0, 0)]
        for cr, cg, cb in cost:
            pr, pg, pb = acc[-1]
            r = min(pg, pb) + cr
            g = min(pr, pb) + cg
            b = min(pr, pg) + cb
            acc.append((r, g, b))
        return min(acc[-1])


n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
answer = Solution().get_answer(n, cost)
print(answer)
