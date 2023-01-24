# 371. Sum of Two Integers
# Link: https://leetcode.com/problems/sum-of-two-integers/
# Difficulty: Medium
# Category: Math
# Category: Bit Manipulation


# Solution 1: bit manipulation, full adder
# Time: 23 ms
# Memory: 14.1 MB
class Solution1:
    def getSum(self, a: int, b: int) -> int:
        BIT_MAX = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        r, n, c = 0, 1, 0
        for _ in range(32):  # calculate 32 bits
            s, c = (a ^ b ^ c) & 1, ((a & b) | (a & c) | (b & c)) & 1
            r = r | s * n
            a, b, n = a >> 1, b >> 1, n << 1

        if r > INT_MAX:  # if the number is negative
            r = ~(r ^ (BIT_MAX))  # bitwise NOT with 32 bit limit twice

        return r


# Solution 2: bit manipulation, bit shifting, binary number
# Time: 36 ms
# Memory: 13.9 MB
class Solution2:
    def getSum(self, a: int, b: int) -> int:
        BIT_MAX = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b:
            a, b = (a ^ b) & BIT_MAX, ((a & b) << 1) & BIT_MAX

        if a > INT_MAX:
            a = ~(a ^ (BIT_MAX))

        return a
