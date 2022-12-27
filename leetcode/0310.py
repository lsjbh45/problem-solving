# 310. Minimum Height Trees
# Link: https://leetcode.com/problems/minimum-height-trees/
# Difficulty: Medium
# Category: Depth-First Search
# Category: Breadth-First Search
# Category: Graph
# Category: Topological Sort
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1:
# Time: 8038 ms (O(n^2))
# Memory: 27 MB
class Solution1:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjs = {i: set() for i in range(n)}
        for n1, n2 in edges:
            adjs[n1].add(n2)
            adjs[n2].add(n1)

        while len(adjs) > 2:
            delList = []
            for n in adjs.keys():
                if len(adjs[n]) == 1:
                    delList.append((n, adjs[n].pop()))

            for d, n in delList:
                adjs.pop(d)
                adjs[n].remove(d)

        return list(adjs.keys())


# Solution 2: bfs topological sort
# Time: 542 ms (O(n))
# Memory: 25.8 MB (O(n))
class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjs = {i: set() for i in range(n)}
        for n1, n2 in edges:
            adjs[n1].add(n2)
            adjs[n2].add(n1)

        nextDelList = [n for n, a in adjs.items() if len(a) == 1]
        while len(adjs) > 2:
            delList, nextDelList = nextDelList, []

            for d in delList:
                n = adjs[d].pop()
                adjs.pop(d)

                adjs[n].remove(d)
                if len(adjs[n]) == 1:
                    nextDelList.append(n)

        return list(adjs.keys())
