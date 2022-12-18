# 743. Network Delay Time
# Link: https://leetcode.com/problems/network-delay-time/
# Difficulty: Medium
# Category: Depth-First Search
# Category: Breadth-First Search
# Category: Graph
# Category: Heap (Priority Queue)
# Category: Shortest Path
from typing import List, Dict, Tuple
import sys
import heapq


# Solution 1: Dijkstra
# Time: 456 ms
# Memory: 16.9 MB
class Solution1:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(graph: Dict[int, List[Tuple[int, int]]],
                     start: int) -> Dict[int, int]:
            dists: Dict[int, int] = {u: sys.maxsize for u in graph}
            dists[start] = 0

            pq: List[Tuple[int, int]] = []
            heapq.heappush(pq, (dists[k], k))

            while pq:
                dist, node = heapq.heappop(pq)
                if dist > dists[node]:
                    continue

                for target, weight in graph[node]:
                    if dist + weight < dists[target]:
                        dists[target] = dist + weight
                        heapq.heappush(pq, (dists[target], target))

            return dists

        graph = {u: [] for u in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        result = max(dijkstra(graph, k).values())
        return -1 if result == sys.maxsize else result
