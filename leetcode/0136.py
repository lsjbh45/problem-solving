# 136. Single Number
# Link: https://leetcode.com/problems/single-number/
# Difficulty: Easy
# Category: Array
# Category: Bit Manipulation
from typing import List


# Solution 1: bit manipulation (xor)
# Time: 150 ms
# Memory: 16.8 MB
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
