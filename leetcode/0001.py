# 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Category: Array
# Category: Hash Table
from typing import List


# Solution 1: brute-force
# Time: 3853 ms (O(n^2))
# Memory: 14.9 MB
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# Solution 2: in
# Time: 730 ms (O(n^2))
# Memory: 15 MB
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums[i + 1:]:
                return [i, nums[i + 1:].index(complement) + (i + 1)]
        return []


# Solution 3: dictionary
# Time: 70 ms (O(n))
# Memory: 15.2 MB
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, n in enumerate(nums):
            if target - n in nums_dict:
                return [i, nums_dict[target - n]]
            nums_dict[n] = i
        return []


# Solution 4: two pointer
# Time: 95 ms (O(n log n))
# Memory: 15.4 MB
class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_enum = list(enumerate(nums))
        nums_enum.sort(key=lambda x: x[1])

        idx1, idx2 = 0, len(nums) - 1
        while idx1 < idx2:
            if nums_enum[idx1][1] + nums_enum[idx2][1] == target:
                return [nums_enum[idx1][0], nums_enum[idx2][0]]
            elif nums_enum[idx1][1] + nums_enum[idx2][1] > target:
                idx2 -= 1
            else:
                idx1 += 1

        return []
