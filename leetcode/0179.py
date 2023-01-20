# 179. Largest Number
# Link: https://leetcode.com/problems/largest-number/
# Difficulty: Medium
# Category: Array
# Category: String
# Category: Greedy
# Category: Sorting
from functools import cmp_to_key
from typing import List


# Solution 1: implement sorting
# Time: 57 ms
# Memory: 13.8 MB
class Solution1:
    @staticmethod
    def cmp(a, b):
        return a + b > b + a

    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(num) for num in nums]
        for i in range(1, len(strs)):
            for j in range(i, 0, -1):
                if self.cmp(strs[j - 1], strs[j]):
                    break
                strs[j - 1], strs[j] = strs[j], strs[j - 1]
        return str(int(''.join(strs)))


# Solution 2: cmp_to_key
# Time: 38 ms
# Memory: 13.9 MB
class Solution2:
    @staticmethod
    def cmp(s1, s2):
        return int(s1 + s2) - int(s2 + s1)

    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(num) for num in nums]
        strs.sort(key=cmp_to_key(self.cmp), reverse=True)
        print(strs)
        return '0' if strs[0] == '0' else ''.join(strs)
