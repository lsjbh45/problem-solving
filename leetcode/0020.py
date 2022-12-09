# 20. Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Category: String
# Category: Stack


# Solution 1: stack
# Time: 30 ms
# Memory: 13.8 MB
class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False
                pair = stack.pop()
                if not (
                    (char == ')' and pair == '(') or
                    (char == '}' and pair == '{') or
                    (char == ']' and pair == '[')
                ):
                    return False
        return not stack


# Solution 2: stack + mapping table
# Time: 53 ms
# Memory: 13.9 MB
class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif not stack or mapping[char] != stack.pop():
                return False
        return not stack


print(Solution2().isValid('()'))
