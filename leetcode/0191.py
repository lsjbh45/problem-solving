# 191. Number of 1 Bits
# Link: https://leetcode.com/problems/number-of-1-bits/
# Difficulty: Easy
# Category: Divide and Conquer
# Category: Bit Manipulation


# Solution 1: stringified number
# Time: 49 ms
# Memory: 13.8 MB
class Solution1:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# Solution 2: bit manipulation, binary number
# Time: 56 ms
# Memory: 13.9 MB
class Solution2:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= (n - 1)
            cnt += 1
        return cnt
