# 33. Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium
# Category: Array
# Category: Binary Search
from typing import List


# Solution 1: find pivot
# Time: 43 ms
# Memory: 14.6 MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(start, end):
            mid = start + (end - start) // 2
            if nums[start] > nums[mid]:
                return findPivot(start, mid)
            elif nums[mid] > nums[end]:
                return findPivot(mid + 1, end)
            else:
                return start

        def binarySearch(start, end):
            if start > end:
                return -1
            mid = start + (end - start) // 2
            if nums[mid % len(nums)] < target:
                return binarySearch(mid + 1, end)
            elif nums[mid % len(nums)] > target:
                return binarySearch(start, mid - 1)
            else:
                return mid % len(nums)

        pivot = findPivot(0, len(nums) - 1)
        return binarySearch(pivot, pivot + len(nums) - 1)
