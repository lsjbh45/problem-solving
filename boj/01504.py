# 1504, 최소비용 구하기
# Link: https://www.acmicpc.net/problem/1504
# Difficulty: Gold 4
# Category: 그래프 이론
# Category: 데이크스트라
# Category: 최단 경로
from typing import List, Dict, Tuple
import heapq
import sys
input = sys.stdin.readline


# Solution 1: dijkstra
# Time: 540 ms
# Memory: 95464 KB
class Solution:
    def dijkstra(self, graph: Dict[int, List[Tuple[int, int]]], start: int) -> List[int]:
        dist = [sys.maxsize for _ in range(len(graph))]
        dist[start] = 0

        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            d, k = heapq.heappop(pq)
            if dist[k] < d:
                continue
            for t, l in graph[k]:
                if l + d < dist[t]:
                    dist[t] = l + d
                    heapq.heappush(pq, (l + d, t))

        return dist

    def get_answer(self, n: int, e: int, vert: List[List[int]], v1: int, v2: int):
        edges = {i: [] for i in range(n)}
        for x, y, c in vert:
            edges[y - 1].append((x - 1, c))
            edges[x - 1].append((y - 1, c))

        v1_dist = self.dijkstra(edges, v1 - 1)
        v2_dist = self.dijkstra(edges, v2 - 1)

        dist = min(v1_dist[0] + v2_dist[n - 1],
                   v1_dist[n - 1] + v2_dist[0]) + v1_dist[v2 - 1]
        return dist if dist < sys.maxsize else - 1


n, e = map(int, input().split())
vert = [list(map(int, input().split())) for _ in range(e)]
v1, v2 = map(int, input().split())
answer = Solution().get_answer(n, e, vert, v1, v2)
print(answer)
