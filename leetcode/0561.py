# 15. 3Sum
# Link: https://leetcode.com/problems/array-partition/
# Difficulty: Easy
# Category: Array
# Category: Greedy
# Category: Sorting
# Category: Counting Sort
from typing import List


# Solution 1: sorting
# Time: 583 ms (O(n log n))
# Memory: 16.9 MB
class Solution1:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
