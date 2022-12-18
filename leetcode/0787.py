# 787. Cheapest Flights Within K Stops
# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Difficulty: Medium
# Category: Dynamic Programming
# Category: Depth-First Search
# Category: Breadth-First Search
# Category: Graph
# Category: Heap (Priority Queue)
# Category: Shortest Path
from typing import List
import heapq
import sys


# Solution 1: pre-calculate available steps for all vertices
# Time: 155 ms
# Memory: 15.3 MB
class Solution1:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, k: int) -> int:
        def dijkstra_step(graph, steps, src):
            dists = {u: sys.maxsize for u in graph}
            dists[src] = 0

            pq = []
            heapq.heappush(pq, (dists[src], src, 0))

            while pq:
                dist, node, step = heapq.heappop(pq)
                if dist > dists[node]:
                    continue

                for target, weight in graph[node]:
                    if target in steps and steps[target] < step + 1:
                        continue

                    if dist + weight < dists[target]:
                        dists[target] = dist + weight
                        heapq.heappush(pq, (dists[target], target, step + 1))

            return dists

        graph = {u: [] for u in range(n)}
        for u, v, w in flights:
            graph[u].append((v, 1))

        min_steps = dijkstra_step(graph, {}, src)
        possible_steps = {u: k + 1 - s for u, s in min_steps.items()}

        graph = {v: [] for v in range(n)}
        for u, v, w in flights:
            graph[v].append((u, w))
        result = dijkstra_step(graph, possible_steps, dst)[src]

        return result if result < sys.maxsize else -1


# Solution 2: consider additional cases with fewer steps for a vertex
# Time: 254 ms
# Memory: 15.4 MB
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, k: int) -> int:
        graph = {u: [] for u in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))

        min_steps = {u: sys.maxsize for u in range(n)}
        pq = [(0, src, 0)]

        while pq:
            dist, node, step = heapq.heappop(pq)

            if node == dst:
                return dist

            if step > k:
                continue

            if step >= min_steps[node]:
                continue

            min_steps[node] = step

            for target, weight in graph[node]:
                heapq.heappush(pq, (dist + weight, target, step + 1))

        return -1
