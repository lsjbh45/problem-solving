# 75. Sort Colors
# Link: https://leetcode.com/problems/sort-colors
# Difficulty: Medium
# Category: Array
# Category: Two Pointers
# Category: Sorting
from typing import List


# Solution 1: insertion sort
# Time: 36 ms
# Memory: 13.9 MB
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1


# Solution 2: dutch national flag (quicksort with three-way partitioning)
# Time: 25 ms
# Memory: 13.9 MB
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                red, white = red + 1, white + 1
            elif nums[white] > 1:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue = blue - 1
            else:
                white = white + 1
