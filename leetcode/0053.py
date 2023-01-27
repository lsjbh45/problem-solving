# 53. Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Category: Array
# Category: Divide and Conquer
# Category: Dynamic Programming
from typing import List


# Solution 1: dynamic programming, Kadane's algorithm
# Time: 917 ms (O(n))
# Memory: 28.7 MB
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, result = 0, -(10 ** 4) - 1
        for num in nums:
            curr = num + (curr if curr > 0 else 0)
            result = max(result, curr)
        return result
