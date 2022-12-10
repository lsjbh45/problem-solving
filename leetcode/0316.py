# 316. Remove Duplicate Letters
# Link: https://leetcode.com/problems/remove-duplicate-letters/
# Difficulty: Medium
# Category: String
# Category: Stack
# Category: Greedy
# Category: Monotonic Stack


# Solution 1: recursion
# Time: 126 ms
# Memory: 14.1 MB
class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ''

        letters = set(s)
        for letter in sorted(letters):
            idx = s.index(letter)
            if set(s) == set(s[idx:]):
                substr = s[idx:].replace(letter, '')
                return letter + self.removeDuplicateLetters(substr)

        return ''


# Solution 2: stack
# Time: 39 ms
# Memory: 13.7 MB
class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        for idx in range(len(s)):
            char = s[idx]
            if char not in stack:
                while stack and char < stack[-1] and stack[-1] in s[idx:]:
                    stack.pop()
                stack.append(char)

        return ''.join(stack)
