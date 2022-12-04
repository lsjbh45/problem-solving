# 125. Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Category: String
# Category: Two Pointers
from collections import deque
from typing import Deque
import re


# Solution 1: deque
# Time: 61 ms
# Memory: 14.8 MB
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        numeric = '0123456789'
        alphanumeric = uppercase + lowercase + numeric

        chars = deque(s)

        while True:
            c1 = '@'
            while c1 not in alphanumeric:
                if not chars:
                    return True
                c1 = chars.popleft()

            c2 = '@'
            while c2 not in alphanumeric:
                if not chars:
                    return True
                c2 = chars.pop()

            if c1 in uppercase:
                c1 = lowercase[uppercase.find(c1)]
            if c2 in uppercase:
                c2 = lowercase[uppercase.find(c2)]
            if c1 != c2:
                return False


# Solution 2: deque + preprocessing
# Time: 117 ms
# Memory: 19.2 MB
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        chars: Deque = deque()

        for char in s:
            if char.isalnum():
                chars.append(char.lower())

        while len(chars) > 1:
            if chars.popleft() != chars.pop():
                return False

        return True


# Solution 3: regex + string slicing
# Time: 87 ms
# Memory: 15.4 MB
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


# Solution 4: two pointer
# Time: 174 ms
# Memory: 14.4 MB
class Solution4:
    def isPalindrome(self, s: str) -> bool:
        bias_left = 0
        bias_right = 1
        str_len = len(s)

        for i in range(str_len):
            while not s[i + bias_left].isalnum():
                bias_left += 1
                if i + bias_left == str_len:
                    return True

            while not s[str_len - i - bias_right].isalnum():
                bias_right += 1

            if i + bias_left >= str_len - i - bias_right:
                break

            if s[i + bias_left].lower() != s[str_len - i - bias_right].lower():
                return False

        return True
