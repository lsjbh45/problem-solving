# 11660. 구간 합 구하기 5
# Link: https://www.acmicpc.net/problem/11660
# Difficulty: Silver 1
# Category: 다이나믹 프로그래밍
# Category: 누적 합
from typing import List, Tuple
import sys
input = sys.stdin.readline


# Solution 1: dynamic programming
# Time: 912 ms
# Memory: 134520 KB
class Solution:
    def get_answer(self, n: int, table: List[List[int]],
                   need: List[Tuple[int, int, int, int]]) -> List[int]:
        acc = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                acc[i + 1][j + 1] = table[i][j] \
                    + acc[i + 1][j] + acc[i][j + 1] - acc[i][j]

        return [
            acc[x2][y2] + acc[x1 - 1][y1 - 1]
            - acc[x1 - 1][y2] - acc[x2][y1 - 1]
            for x1, y1, x2, y2 in need
        ]


n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
need = [tuple(map(int, input().split())) for _ in range(m)]
answer = Solution().get_answer(n, table, need)
for result in answer:
    print(result)
