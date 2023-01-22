# 349. Intersection of Two Arrays
# Link: https://leetcode.com/problems/intersection-of-two-arrays/
# Difficulty: Easy
# Category: Array
# Category: Hash Table
# Category: Two Pointers
# Category: Binary Search
# Category: Sorting
from typing import List
import bisect


# Solution 1: two pointers
# Time: 42 ms
# Memory: 14.1 MB
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        idx = 0
        intersects = [-1]
        for num in nums1:
            while num > nums2[idx] and idx < len(nums2) - 1:
                idx += 1
            if num == nums2[idx] and num != intersects[-1]:
                intersects.append(num)

        return intersects[1:]


# Solution 2: binary search, set
# Time: 51 ms
# Memory: 14.1 MB
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        result = set()
        for num in nums2:
            idx = bisect.bisect_left(nums1, num)
            if idx < len(nums1) and nums1[idx] == num:
                result.add(num)
        return list(result)
