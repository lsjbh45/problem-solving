# 208. Implement Trie (Prefix Tree)
# Link: https://leetcode.com/problems/implement-trie-prefix-tree/
# Difficulty: Medium
# Category: Hash Table
# Category: String
# Category: Design
# Category: Trie


# Solution 1: dictionary
# Time: 120 ms
# Memory: 27.5 MB
class Trie:
    def __init__(self):
        self.data = {}

    def insert(self, word: str) -> None:
        node = self.data
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['exists'] = True

    def search(self, word: str) -> bool:
        node = self.data
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return 'exists' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.data
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
