# 169. Majority Element
# Link: https://leetcode.com/problems/majority-element/
# Difficulty: Easy
# Category: Array
# Category: Hash Table
# Category: Divide and Conquer
# Category: Sorting
# Category: Counting
from typing import List, Tuple


# Solution 1: divide and conquer
# Time: 437 ms
# Memory: 16.1 MB
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        def findMajority(s, e) -> Tuple[int, int]:
            if s == e:
                return nums[s], 1

            m = s + (e - s) // 2
            (an, ac), (bn, bc) = findMajority(s, m), findMajority(m + 1, e)

            if an and bn:
                if an == bn:
                    return an, ac + bc
                if ac > bc:
                    return an, ac - bc
                elif ac < bc:
                    return bn, bc - ac
                else:
                    return 0, 0
            return an or bn, ac or bc
        return findMajority(0, len(nums) - 1)[0]


# Solution 2: divide and conquer
# Time: 529 ms
# Memory: 15.8 ms
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        def findMajority(s, e) -> int:
            if s == e:
                return nums[s]

            m = s + (e - s) // 2
            a, b = findMajority(s, m), findMajority(m + 1, e)

            return a if nums[s:e+1].count(a) > (e - s) // 2 else b
        return findMajority(0, len(nums) - 1)


# Solution 3: sorting
# Time: 210 ms
# Memory: 15.4 MB
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


# Solution 4:
# Time: 164 ms (O(n))
# Memory: 15.5 MB (O(1))
class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = -1, 0
        for num in nums:
            if count == 0:
                major, count = num, 1
            else:
                count += (1 if num == major else -1)
        return major
