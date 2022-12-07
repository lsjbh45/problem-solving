# 15. 3Sum
# Link: https://leetcode.com/problems/3sum/
# Difficulty: Medium
# Category: Array
# Category: Two Pointers
# Category: Sorting
from typing import List, Set, Dict, Tuple


# Solution 1: dictionary
# Time: 1143 ms (O(n^2))
# Memory: 19 MB
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counts: Dict[int, int] = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        distinctNums: List[int] = list(counts.keys())
        threeSums: Dict[Tuple[int, int, int], None] = {}
        for num1 in distinctNums:
            for num2 in distinctNums:
                num3 = -(num1 + num2)
                if num3 in counts:
                    if num1 == num3 or num2 == num3:
                        if counts[num3] < 2:
                            continue
                    if num1 == num2:
                        if counts[num2] < 2:
                            continue
                    if num1 == num3 and num2 == num3:
                        if counts[num3] < 3:
                            continue
                    threeSum = tuple(sorted((num1, num2, num3)))
                    if threeSum not in threeSums:
                        threeSums[threeSum] = None

        return [list(threeSum) for threeSum in threeSums]


# Solution 2: two pointers
# Time: 985 ms (O(n^2))
# Memory: 19.1 MB
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results: Set[Tuple[int, int, int]] = set()
        nums.sort()

        for i in range(len(nums) - 2):
            # check duplication of first number
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            num1 = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                num2, num3 = nums[left], nums[right]
                if num2 + num3 == -num1:
                    results.add(tuple(sorted((num1, num2, num3))))
                    left, right = left + 1, right - 1
                elif num2 + num3 > -num1:
                    right -= 1
                else:
                    left += 1

        return [list(result) for result in results]
