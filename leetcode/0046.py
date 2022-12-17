# 46. Permutations
# Link: https://leetcode.com/problems/permutations/
# Difficulty: Medium
# Category: Array
# Category: Backtracking
from typing import List
import itertools


# Solution 1: dfs
# Time: 40 ms
# Memory: 13.2 MB
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: List[List[int]] = []
        last_permutation: List[int] = []

        def dfs(nums: List[int]):
            if not nums:
                permutations.append(last_permutation[:])
                return

            for num in nums:
                next_nums = nums[:]
                next_nums.remove(num)

                last_permutation.append(num)
                dfs(next_nums)
                last_permutation.pop()

        dfs(nums)
        return permutations


# Solution 2: itertools
# Time: 34 ms
# Memory: 14 MB
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in itertools.permutations(nums)]
