# 242. Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Category: Hash Table
# Category: String
# Category: Sorting


# Solution 1: sorting
# Time: 52 ms
# Memory: 15.2 MB
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
