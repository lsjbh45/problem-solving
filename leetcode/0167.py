# 167. Two Sum II - Input Array Is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Medium
# Category: Array
# Category: Two Pointers
# Category: Binary Search
from typing import List
import bisect


# Solution 1: two pointers
# Time: 135 ms
# Memory: 15 MB
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return []


# Solution 2: binary search with boundary
# Time: 139 ms
# Memory: 15 MB
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for (idx1, num) in enumerate(numbers):
            idx2 = bisect.bisect_left(numbers, target - num, idx1 + 1)
            if idx2 < len(numbers) and target - num == numbers[idx2]:
                return [idx1 + 1, idx2 + 1]
        return []
