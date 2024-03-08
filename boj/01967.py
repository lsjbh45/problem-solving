# 1967. 트리의 지름
# Link: https://www.acmicpc.net/problem/1967
# Difficulty: Gold 4
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 트리
# Category: 깊이 우선 탐색
from typing import List, Tuple
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


# Solution 1: recursion
# Time: 188 ms
# Memory: 47502 MB
class Solution:
    def get_answer(self, n: int, edges: List[List[int]]) -> int:
        graph = {v: [] for v in range(n)}
        for v, w, c in edges:
            graph[v - 1].append((w - 1, c))

        def get_max(n: int) -> Tuple[int, int]:
            paths = []
            max_path = max_diam = 0

            for child, cost in graph[n]:
                path, diam = get_max(child)
                heapq.heappush(paths, -(cost + path))
                max_diam = max(max_diam, diam)

            if paths:
                max_path = -heapq.heappop(paths)
                if paths:
                    max_diam = max(max_diam, max_path - heapq.heappop(paths))

            return (max_path, max_diam)

        path, diam = get_max(0)
        return max(path, diam)


n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
answer = Solution().get_answer(n, edges)
print(answer)
