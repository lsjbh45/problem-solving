# 1865. 웜홀
# Link: https://www.acmicpc.net/problem/1865
# Difficulty: Gold 3
# Category: 그래프 이론
# Category: 최단 경로
# Category: 벨만–포드
from typing import List, Tuple


# Solution 1: bellman-ford
# Time: 1416 ms
# Memory: 38848 KB
class Solution:
    def get_answer(self, n: int, m: int, w: int,
                   roads: List[List[int]], holes: List[List[int]]) -> bool:

        def bellman_ford_all(v: int, e: int, edges: Tuple[int, int, int]) -> bool:
            dists = [0 for _ in range(v)]

            for i in range(v):
                for a, b, t in edges:
                    if dists[a] + t < dists[b]:
                        dists[b] = dists[a] + t
                        if i == v - 1:
                            return True

            return False

        edges = [
            *(list(map(lambda edge: (edge[0] - 1, edge[1] - 1, edge[2]), roads))),
            *(list(map(lambda edge: (edge[1] - 1, edge[0] - 1, edge[2]), roads))),
            *(list(map(lambda edge: (edge[0] - 1, edge[1] - 1, -edge[2]), holes))),
        ]
        return bellman_ford_all(n, 2 * m + w, edges)


tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    holes = [list(map(int, input().split())) for _ in range(w)]
    answer = Solution().get_answer(n, m, w, roads, holes)
    print('YES' if answer else 'NO')
