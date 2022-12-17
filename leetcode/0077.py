# 77. Combinations
# Link: https://leetcode.com/problems/combinations/
# Difficulty: Medium
# Category: Backtracking
from typing import List
import itertools


# Solution 1: itertools
# Time: 83 ms
# Memory: 15.8 MB
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(c) for c in itertools.combinations(range(1, n + 1), k)]


# Solution 2: dfs
# Time: 90 ms
# Memory: 15.9 MB
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations: List[List[int]] = []
        combination: List[int] = []

        def dfs():
            if len(combination) == k:
                combinations.append(combination[:])
                return

            if k - len(combination) > (n - combination[-1]):
                return

            for i in range(combination[-1] + 1, n + 1):
                combination.append(i)
                dfs()
                combination.pop()

        for i in range(1, n + 1):
            combination = [i]
            dfs()

        return combinations
