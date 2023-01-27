# 198. House Robber
# Link: https://leetcode.com/problems/house-robber/
# Difficulty: Medium
# Category: Array
# Category: Dynamic Programming
from typing import List


# Solution 1: dynamic programming
# Time: 32 ms
# Memory: 13.8 MB
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, nums.pop(0)]

        for num in nums:
            dp.append(max(dp[-1], dp[-2] + num))

        return dp[-1]
