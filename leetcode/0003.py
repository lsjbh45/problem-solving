# 3. Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Category: Hash Table
# Category: String
# Category: Sliding Window


# Solution 1:
# Time: 58 ms
# Memory: 14.1 MB
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        substr = ''
        for char in s:
            if char in substr:
                max_length = max(max_length, len(substr))
                substr = substr[substr.index(char)+1:]
            substr += char
        return max(max_length, len(substr))


# Solution 2: sliding window, two pointer, hash table
# Time: 60 ms
# Memory: 14.1 MB
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        last_index = {}

        for index, char in enumerate(s):
            if char in last_index and start <= last_index[char]:
                start = last_index[char] + 1
            last_index[char] = index
            max_length = max(max_length, index - start + 1)

        return max_length
