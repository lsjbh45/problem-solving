# 76. Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/
# Difficulty: Hard
# Category: Hash Table
# Category: String
# Category: Sliding Window
from collections import deque, Counter


# Solution 1: two pointer, sliding window
# Time: 936 ms
# Memory: 14.8 MB
class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            if char not in need:
                need[char] = 0
            need[char] += 1

        start = end = -1
        left = 0

        for right, char in enumerate(s):
            if char in need:
                need[char] -= 1
                if all(n <= 0 for n in need.values()):
                    while left < right and \
                            (s[left] not in need or need[s[left]] < 0):
                        if s[left] in need:
                            need[s[left]] += 1
                        left += 1
                    if start == -1 or (end - start) > (right - left):
                        start, end = left, right
                        need[s[left]] += 1
                        left += 1

        return s[start:end+1]


# Solution 2: deque, Counter
# Time: 352 ms
# Memory: 14.7 MB
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        cnt = Counter()

        min_window = ''
        window = deque()
        for char in s:
            cnt[char] += 1
            window.append(char)

            if all(cnt[c] >= need[c] for c in need.keys()):
                while window and cnt[window[0]] > need[window[0]]:
                    c = window.popleft()
                    cnt[c] -= 1
                if not min_window or len(window) < len(min_window):
                    min_window = ''.join(window)
                if window:
                    cnt[window.popleft()] -= 1

        return min_window
