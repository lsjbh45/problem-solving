# 455. Assign Cookies
# Link: https://leetcode.com/problems/assign-cookies/
# Difficulty: Easy
# Category: Array
# Category: Two Pointers
# Category: Greedy
# Category: Sorting
import bisect
from typing import List


# Solution 1: greedy algorithm
# Time: 473 ms
# Memory: 16 MB
class Solution1:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cnt = 0
        idx = 0

        for c in g:
            while idx < len(s):
                if c <= s[idx]:
                    cnt += 1
                    idx += 1
                    break
                idx += 1
        return cnt


# Solution 2: binary search
# Time: 483 ms
# Memory: 15.8 MB
class Solution2:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cnt = 0

        for i in s:
            if bisect.bisect_right(g, i) > cnt:
                cnt += 1

        return cnt
