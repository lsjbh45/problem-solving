# 5. Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty: Medium
# Category: String
# Category: Dynamic Programming
from typing import List


# Solution 1: expand around center
# Time: 2588 ms (O(n^2))
# Memory: 15.5 MB (O(1))
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        palindromes = []

        def getPalindrome(start, end):
            if s[start] == s[end]:
                if start >= 1 and end <= length - 2:
                    return getPalindrome(start - 1, end + 1)
                else:
                    return s[start:end+1]
            else:
                return s[start+1:end]

        for idx in range(length):
            palindromes.append(getPalindrome(idx, idx))

        for idx in range(length - 1):
            palindromes.append(getPalindrome(idx, idx + 1))

        return max(palindromes, key=len)


# Solution 2: dynamic programming
# Time: 5233 ms (O(n^2))
# Memory: 22.7 MB (O(n^2))
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        longest: str = ''
        isPalindrome: List[List[bool]] = [
            [False for _ in range(len(s))] for _ in range(len(s))
        ]

        for i in range(len(s)):
            isPalindrome[i][i] = True
            longest = s[i]

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                isPalindrome[i][i + 1] = True
                longest = s[i:i+2]

        for i in range(2, len(s)):
            for j in range(len(s) - i):
                a, b = j, i + j
                if isPalindrome[a + 1][b - 1] and s[a] == s[b]:
                    isPalindrome[a][b] = True
                    longest = s[a:b+1]

        return longest


# Solution 3: longest common substring
# Time: 6925 ms (O(n^2))
# Memory: 40 MB (O(n^2))
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        s_rev = s[::-1]
        common_len: List[List[int]] = [
            [0 for _ in range(len(s))] for _ in range(len(s))
        ]
        max_common_len = 0
        max_common_str = ''

        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s_rev[j]:
                    common_len[i][j] = (
                        common_len[i-1][j-1] if i and j else 0
                    ) + 1
                    if common_len[i][j] > max_common_len:
                        # check index
                        if i - common_len[i][j] + 1 == len(s) - 1 - j:
                            max_common_len = common_len[i][j]
                            max_common_str = s[i - common_len[i][j] + 1:i + 1]

        return max_common_str


print(Solution3().longestPalindrome(s="cbba"))
