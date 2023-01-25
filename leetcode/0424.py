# 424. Longest Repeating Character Replacement
# Link: https://leetcode.com/problems/longest-repeating-character-replacement
# Difficulty: Medium
# Category: Hash Table
# Category: String
# Category: Sliding Window
from collections import Counter


# Solution 1: two pointer, sliding window
# Time: 120 ms
# Memory: 14 MB
class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        cnt = Counter()

        for right, char in enumerate(s):
            cnt[char] += 1
            common_cnt = max(cnt.values())

            if right - left + 1 > k + common_cnt:
                cnt[s[left]] -= 1
                left += 1

        return right - left + 1
