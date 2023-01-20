# 56. Merge Intervals
# Link: https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium
# Category: Array
# Category: Sorting
from typing import List


# Solution 1: sort and merge
# Time: 151 ms
# Memory: 18 MB
class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = []
        for interval in intervals:
            if result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result
