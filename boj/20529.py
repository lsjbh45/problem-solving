# 20529. 가장 가까운 세 사람의 심리적 거리
# Link: https://www.acmicpc.net/problem/20529
# Difficulty: Silver 1
# Category: 브루트포스 알고리즘
# Category: 비둘기집 원리
from typing import List, Tuple
from collections import Counter
from itertools import combinations


# Solution 1: brute-force, counter
# Time: 848 ms
# Memory: 44716 KB
class Solution1:
    def get_2_len(self, mbti1: str, mbti2: str) -> int:
        return sum(char1 != char2 for char1, char2 in zip(mbti1, mbti2))

    def get_3_len(self, comb: Tuple[str, str, str]) -> int:
        return sum(self.get_2_len(mbti1, mbti2) for mbti1, mbti2 in combinations(comb, 2))

    def get_answer(self, n: int, mbtis: List[str]) -> int:
        counts = Counter(mbtis).most_common()
        if counts[0][1] >= 3:
            return 0

        return min(self.get_3_len(comb) for comb in combinations(mbtis, 3))


# Solution 2: brute-force, pigeonhole principle
# Time: 844 ms
# Memory: 44716 KB
class Solution2:
    def get_2_len(self, mbti1: str, mbti2: str) -> int:
        return sum(char1 != char2 for char1, char2 in zip(mbti1, mbti2))

    def get_3_len(self, comb: Tuple[str, str, str]) -> int:
        return sum(self.get_2_len(mbti1, mbti2) for mbti1, mbti2 in combinations(comb, 2))

    def get_answer(self, n: int, mbtis: List[str]) -> int:
        if n > 32:
            return 0

        return min(self.get_3_len(comb) for comb in combinations(mbtis, 3))


t = int(input())
for _ in range(t):
    n = int(input())
    mbtis = list(input().split())
    answer = Solution2().get_answer(n, mbtis)
    print(answer)
