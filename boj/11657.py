# 11657. 타임머신
# Link: https://www.acmicpc.net/problem/11657
# Difficulty: Gold 4
# Category: 그래프 이론
# Category: 최단 경로
# Category: 벨만–포드
from typing import List
from sys import maxsize


# Solution 1: bellman-ford
# Time: 936 ms
# Memory: 38828 MB
class Solution:
    def get_answer(self, n: int, m: int, buses: List[int]) -> List[int] | None:
        dists = [maxsize for _ in range(n)]
        dists[0] = 0

        for i in range(n):
            for a, b, c in buses:
                s, e = a - 1, b - 1
                if dists[s] == maxsize:
                    continue
                if dists[s] + c < dists[e]:
                    dists[e] = dists[s] + c
                    if i == n - 1:
                        return None
        return dists


n, m = map(int, input().split())
buses = [list(map(int, input().split())) for _ in range(m)]
answer = Solution().get_answer(n, m, buses)
if answer is None:
    print(-1)
else:
    print('\n'.join(
        map(lambda x: str(x) if x < maxsize else '-1', answer[1:])
    ))
