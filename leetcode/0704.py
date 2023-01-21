# 704. Binary Search
# Link: https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Category: Array
# Category: Binary Search

from typing import List
import bisect


# Solution 1: recursion
# Time: 260 ms
# Memory: 22.9 MB
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        def rec(start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return rec(start, mid - 1)
            else:
                return rec(mid + 1, end)
        return rec(0, len(nums) - 1)


# Solution 2: bisect
# Time: 239 ms
# Memory: 15.4 MB
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
