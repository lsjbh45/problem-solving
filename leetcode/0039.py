# 39. Combination Sum
# Link: https://leetcode.com/problems/combination-sum/
# Difficulty: Medium
# Category: Array
# Category: Backtracking
from typing import List


# Solution 1: dfs, backtracking
# Time: 68 ms
# Memory: 14 MB
class Solution1:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        results: List[List[int]] = []

        def dfs(nums, candidates):
            if sum(nums) == target:
                results.append(nums)
                return

            for i, n in enumerate(candidates):
                if sum(nums) + n <= target:
                    dfs([*nums, n], candidates[i:])

        for i, n in enumerate(candidates):
            dfs([n], candidates[i:])

        return results
