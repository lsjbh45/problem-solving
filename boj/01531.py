# 1531. 투명
# Link: https://www.acmicpc.net/problem/1531
# Difficulty: Silver 5
# Category: 구현
# Category: 시뮬레이션
from typing import List, Tuple


# Solution 1: brute-force
# Time: 164 ms
# Memory: 38848 KB
class Solution:
    def get_cnt(self, n: int, m: int,
                paper: List[Tuple[int, int, int, int]]) -> int:
        hide = [[0 for _ in range(100)] for _ in range(100)]

        for x1, y1, x2, y2 in paper:
            for i in range(x1 - 1, x2):
                for j in range(y1 - 1, y2):
                    hide[i][j] += 1

        return sum(sum(1 for pic in row if pic > m) for row in hide)


n, m = map(int, input().split())
paper = [tuple(map(int, input().split())) for _ in range(n)]
answer = Solution().get_cnt(n, m, paper)
print(answer)
