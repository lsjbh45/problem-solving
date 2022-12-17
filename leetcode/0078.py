# 78. Subsets
# Link: https://leetcode.com/problems/subsets/
# Difficulty: Medium
# Category: Array
# Category: Backtracking
# Category: Bit Manipulation
from typing import List


# Solution 1: dfs
# Time: 31 ms
# Memory: 14.2 MB
class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = []
        subset = []

        def find(idx):
            if idx == len(nums) - 1:
                subsets.append(subset[:])
                return

            find(idx + 1)
            subset.append(nums[idx])
            find(idx + 1)
            subset.pop()

        find(-1)
        return subsets


# Solution 2: dfs
# Time: 30 ms
# Memory: 14.1 MB
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = []

        def find(idx, subset):
            subsets.append(subset)

            for i in range(idx + 1, len(nums)):
                find(i, subset + [nums[i]])

        find(-1, [])
        return subsets


# Solution 3: bit
# Time: 40 ms
# Memory: 14.1 MB
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[
            num for i, num in enumerate(nums) if (bit // 2 ** i) % 2
        ] for bit in range(2 ** len(nums))]
