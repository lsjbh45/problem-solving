# 56. Merge Intervals
# Link: https://leetcode.com/problems/k-closest-points-to-origin
# Difficulty: Medium
# Category: Array
# Category: Math
# Category: Divide and Conquer
# Category: Geometry
# Category: Sorting
# Category: Heap (Priority Queue)
# Category: Quickselect
from typing import List
import heapq


# Solution 1: sort
# Time: 793 ms
# Memory: 20.5 MB
class Solution1:
    def kClosest(self, points: List[List[int]], k: int) \
            -> List[List[int]]:
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]


# Solution 2: priority queue
# Time: 836 ms
# Memory: 20.3 MB
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) \
            -> List[List[int]]:
        heap = [(x ** 2 + y ** 2, x, y) for x, y in points]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])
        return result
