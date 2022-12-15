# 771. Jewels and Stones
# Link: https://leetcode.com/problems/jewels-and-stones/
# Difficulty: Easy
# Category: Hash Table
# Category: String
from collections import Counter


# Solution 1: Counter
# Time: 39 ms
# Memory: 13.8 MB
class Solution1:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stoneCount = Counter(stones)
        return sum([stoneCount[jewel] for jewel in jewels])


# Solution 2: list comprehension
# Time: 28 ms
# Memory: 13.9 MB
class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum((stone in jewels) for stone in stones)


print(Solution1().numJewelsInStones(jewels="aA", stones="aAAbbbb"))
