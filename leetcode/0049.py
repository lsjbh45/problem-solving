# 49. Reverse String
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Category: String
# Category: Array
# Category: Sorting
# Category: Hash Table
from typing import List
from collections import defaultdict


# Solution 1:
# Time: 223 ms
# Memory: 17.2 MB
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            group = ''.join(sorted(string))
            anagrams[group].append(string)

        return list(anagrams.values())
