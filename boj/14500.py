# 14500. 테트로미노
# Link: https://www.acmicpc.net/problem/14500
# Difficulty: Gold 4
# Category: 구현
# Category: 브루트포스 알고리즘
from typing import List
import sys
input = sys.stdin.readline


# Solution 1: brute-force
# Time: 3140 ms
# Memory: 42016 KB
class Solution:
    def get_answer(self, n: int, m: int, paper: List[List[int]]) -> int:
        max_sum = 0

        tetrominos = {
            (4, 1): [((0, 0), (1, 0), (2, 0), (3, 0))],
            (1, 4): [((0, 0), (0, 1), (0, 2), (0, 3))],
            (2, 2): [((0, 0), (0, 1), (1, 0), (1, 1))],
            (2, 3): [
                ((0, 0), (0, 1), (0, 2), (1, 0)),
                ((0, 0), (0, 1), (0, 2), (1, 2)),
                ((0, 0), (1, 0), (1, 1), (1, 2)),
                ((0, 2), (1, 0), (1, 1), (1, 2)),
                ((0, 0), (0, 1), (0, 2), (1, 1)),
                ((0, 1), (1, 0), (1, 1), (1, 2)),
                ((0, 0), (0, 1), (1, 1), (1, 2)),
                ((0, 1), (0, 2), (1, 0), (1, 1)),
            ],
            (3, 2): [
                ((0, 0), (1, 0), (2, 0), (0, 1)),
                ((0, 0), (1, 0), (2, 0), (2, 1)),
                ((0, 0), (0, 1), (1, 1), (2, 1)),
                ((2, 0), (0, 1), (1, 1), (2, 1)),
                ((0, 0), (1, 0), (2, 0), (1, 1)),
                ((1, 0), (0, 1), (1, 1), (2, 1)),
                ((0, 0), (1, 0), (1, 1), (2, 1)),
                ((1, 0), (2, 0), (0, 1), (1, 1)),
            ],
        }

        for size, cases in tetrominos.items():
            x, y = size
            for i in range(n - x + 1):
                for j in range(m - y + 1):
                    for case in cases:
                        max_sum = max(max_sum, sum(
                            paper[i + a][j + b] for a, b in case
                        ))

        return max_sum


n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = Solution().get_answer(n, m, paper)
print(answer)
