# 393. UTF-8 Validation
# Link: https://leetcode.com/problems/utf-8-validation/
# Difficulty: Medium
# Category: Array
# Category: Bit Manipulation
from typing import List


# Solution 1: bit manipulation
# Time: 145 ms
# Memory: 14.1 MB
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        byte = 0
        for char in data:
            if byte:
                if not (char >> 7 and not char >> 6 & 1):
                    return False
                byte -= 1
            else:
                if char >> 7:
                    if not (char >> 6 & 1):
                        return False
                    byte = 1
                    if char >> 5 & 1:
                        byte += 1
                        if char >> 4 & 1:
                            byte += 1
                            if char >> 3 & 1:
                                return False
        return not byte
