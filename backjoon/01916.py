# 1916, 최소비용 구하기
# Link: https://www.acmicpc.net/problem/1916
# Difficulty: Gold 5
# Category: 그래프 이론
# Category: 데이크스트라
from typing import List, Tuple
import heapq
import sys
input = sys.stdin.readline


# Solution 1: dijkstra
# Time: 316 ms
# Memory: 61088 KB
class Solution:
    def get_answer(self, n: int, m: int,
                   bus: List[Tuple[int, int, int]], s: int, e: int) -> int:
        cost = [[
            0 if x == y else sys.maxsize for y in range(n + 1)
        ] for x in range(n + 1)]
        for x, y, c in bus:
            cost[x][y] = min(cost[x][y], c)

        min_cost = [0 if s == i else sys.maxsize for i in range(n + 1)]

        pq = [(0, s)]
        while pq:
            c, t = heapq.heappop(pq)
            if c != min_cost[t]:
                continue
            for v in range(n + 1):
                if min_cost[v] > min_cost[t] + cost[t][v]:
                    min_cost[v] = min_cost[t] + cost[t][v]
                    heapq.heappush(pq, (min_cost[v], v))

        return min_cost[e]


n = int(input())
m = int(input())
bus = [tuple(map(int, input().split())) for _ in range(m)]
s, e = map(int, input().split())
answer = Solution().get_answer(n, m, bus, s, e)
print(answer)
