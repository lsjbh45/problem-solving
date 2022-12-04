# 344. Reverse String
# Link: https://leetcode.com/problems/reverse-string/
# Difficulty: Easy
# Category: String
# Category: Two Pointers
from typing import List


# Solution 1: slicing
class Solution1:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]  # space complexity: O(1)


# Solution 2: reverse()
# Time: 195 ms
# Space: 18.3 MB
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


# Solution 3: two pointer
# Time: 693 ms
# Space: 18.3 MB
class Solution3:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


Solution3().reverseString(['s', 't', 'r'])
