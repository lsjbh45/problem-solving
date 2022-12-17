# 17. Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Difficulty: Medium
# Category: Hash Table
# Category: String
# Category: Backtracking
from typing import List


# Solution 1: dfs
# Time: 18 ms
# Memory: 13.9 MB
class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        combinations = []

        def getCombinations(digits: str, combination: str = ''):
            if not digits:
                if combination:
                    combinations.append(combination)
                return

            for letter in mapping[digits[0]]:
                getCombinations(digits[1:], combination + letter)

        getCombinations(digits)
        return combinations
