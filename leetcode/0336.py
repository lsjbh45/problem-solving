# 336. Palindrome Pairs
# Link: https://leetcode.com/problems/palindrome-pairs/
# Difficulty: Hard
# Category: Array
# Category: Hash Table
# Category: String
# Category: Trie
from typing import List, Dict, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.word: Optional[int] = None
        self.palindromes: List[int] = []

    def __repr__(self):
        return f'[{str(self.children)}, {self.word}, {self.palindromes}]'


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def insert(self, idx: int, word: str) -> None:
        node = self.root
        for n, char in enumerate(word[::-1]):
            if self.is_palindrome(word[::-1][n:]):
                node.palindromes.append(idx)
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = idx

    def search(self, idx: int, word: str) -> List[List[int]]:
        node = self.root
        pairs = []

        for n, char in enumerate(word):
            if node.word is not None:
                if self.is_palindrome(word[n:]):
                    pairs.append([idx, node.word])
            if char not in node.children:
                return pairs
            node = node.children[char]

        if node.word is not None and idx != node.word:
            pairs.append([idx, node.word])

        for p in node.palindromes:
            pairs.append([idx, p])

        return pairs


# Solution 1: trie
# Time: 5359 ms
# Memory: 388.7 MB
class Solution1:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        pairs = []

        for idx, word in enumerate(words):
            trie.insert(idx, word)

        for idx, word in enumerate(words):
            pairs.extend(trie.search(idx, word))

        return pairs
