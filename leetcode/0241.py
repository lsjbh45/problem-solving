# 241. Different Ways to Add Parentheses
# Link: https://leetcode.com/problems/different-ways-to-add-parentheses/
# Difficulty: Medium
# Category: Math
# Category: String
# Category: Dynamic Programming
# Category: Recursion
# Category: Memoization
from typing import List
import re
import operator


# Solution 1: divide and conquer
# Time: 34 ms
# Memory: 14 MB
class Solution1:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = [int(num) for num in re.split(r'[\+\-\*]', expression)]
        operators = re.split(r'\d+', expression)

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }

        def getResult(s: int, e: int) -> List[int]:
            if s > e:
                return [nums[s - 1]]
            if s == e:
                return [operations[operators[s]](nums[s - 1], nums[s])]

            result = []
            for i in range(s, e + 1):
                r1 = getResult(s, i - 1)
                r2 = getResult(i + 1, e)
                for n1 in r1:
                    for n2 in r2:
                        result.append(operations[operators[i]](n1, n2))
            return result

        return getResult(1, len(operators) - 2)


# Solution 2: divide and conquer
# Time: 145 ms
# Memory: 14.1 MB
class Solution2:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isnumeric():
            return [int(expression)]

        result = []
        for i, x in enumerate(expression):
            if x in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])

                for lv in left:
                    for rv in right:
                        result.append(eval(f'{lv}{x}{rv}'))
        return result
