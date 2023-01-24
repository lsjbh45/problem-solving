# 461. Hamming Distance
# Link: https://leetcode.com/problems/hamming-distance/
# Difficulty: Easy
# Category: Bit Manipulation


# Solution 1: bit manipulation (xor)
# Time: 31 ms
# Memory: 13.8 MB
class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y

        result = 0
        while z:
            result += z & 1
            z >>= 1
        return result


# Solution 2: bit manipulation (xor), stringified number
# Time: 28 ms
# Memory: 13.8 MB
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
