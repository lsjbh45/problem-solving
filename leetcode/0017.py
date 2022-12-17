# 17. Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Difficulty: Medium
# Category: Hash Table
# Category: String
# Category: Backtracking
from typing import List


# Solution 1: traversing
# Time: 18 ms
# Memory: 13.9 MB
class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
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


print(Solution1().letterCombinations(""))
