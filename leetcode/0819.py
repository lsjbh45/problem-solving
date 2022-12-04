# 819. Most Common Word
# Link: https://leetcode.com/problems/most-common-word/
# Difficulty: Easy
# Category: String
# Category: Hash Table
# Category: Counting
from typing import List, Dict, Tuple
from collections import defaultdict, Counter
import re


# Solution 1: dict
# Time: 72 ms
# Memory: 13.9 MB
class Solution1:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub("[ !?',;.]", ' ', paragraph.lower()).split()
        word_cnt: Dict[str, int] = {}

        for word in words:
            if word not in word_cnt:
                word_cnt[word] = 0
            word_cnt[word] += 1

        word_lst: List[Tuple[str, int]] = sorted(
            word_cnt.items(), key=lambda x: x[1], reverse=True)

        for word, _ in word_lst:
            if word not in banned:
                return word


# Solution 2: defaultdict
# Time: 86 ms
# Memory: 16.9 MB
class Solution2:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r'[^\w]', ' ', paragraph.lower()).split()
        words = [word for word in words if word not in banned]

        word_cnt = defaultdict(int)
        for word in words:
            word_cnt[word] += 1

        return max(word_cnt, key=word_cnt.get)


# Solution 3: counter
# Time: 75 ms
# Memory: 16.9 MB
class Solution3:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r'[^\w]', ' ', paragraph.lower()).split()
        words = [word for word in words if word not in banned]

        word_cnt = Counter(words)
        return word_cnt.most_common(1)[0][0]
