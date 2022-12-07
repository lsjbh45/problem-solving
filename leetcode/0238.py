# 238. Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Category: Array
# Category: Prefix Sum

from typing import List


# Solution 1: pre-calculated products
# Time: 1028 ms (O(nk))
# Memory: 21.1 MB (O(k))
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == 1:
            idx = nums.index(0)
            prod = 1
            for i in range(len(nums)):
                if i != idx:
                    prod *= nums[i]
                    nums[i] = 0
            nums[idx] = prod
            return nums
        elif nums.count(0) >= 2:
            return [0 for _ in range(len(nums))]
        else:
            prods = {key: [1, False] for key in range(-30, 31)}
            for num in nums:
                for key in range(-30, 31):
                    if key == num and not prods[key][1]:
                        prods[key][1] = True
                    else:
                        prods[key][0] *= num
            return [prods[key][0] for key in nums]


# Solution 2: prefix products (prefix sum)
# Time: 610 ms (O(n))
# Memory: 21.2 MB (O(1))
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        left_prod = 1
        for i in range(len(nums)):
            out.append(left_prod)
            left_prod *= nums[i]

        right_prod = 1
        for j in range(len(nums) - 1, -1, -1):
            out[j] *= right_prod
            right_prod *= nums[j]

        return out
