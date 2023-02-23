# 2096. 내려가기
# Link: https://www.acmicpc.net/problem/2096
# Difficulty: Gold 5
# Category: 다이나믹 프로그래밍
# Category: 슬라이딩 윈도우
from typing import Tuple
import sys
input = sys.stdin.readline


def input_generator(n):
    for _ in range(n):
        yield tuple(map(int, input().split()))


# Solution 1: dynamic programming
# Time: 352 ms
# Memory: 38900 KB
class Solution:
    def get_answer(self, gen) -> Tuple[int, int]:
        max_acc, min_acc = (0, 0, 0), (0, 0, 0)
        for n1, n2, n3 in gen:
            max_acc = (
                max(max_acc[0], max_acc[1]) + n1,
                max(max_acc[0], max_acc[1], max_acc[2]) + n2,
                max(max_acc[1], max_acc[2]) + n3,
            )
            min_acc = (
                min(min_acc[0], min_acc[1]) + n1,
                min(min_acc[0], min_acc[1], min_acc[2]) + n2,
                min(min_acc[1], min_acc[2]) + n3,
            )
        return (max(max_acc), min(min_acc))


n = int(input())
gen = input_generator(n)
answer = Solution().get_answer(gen)
print(*answer)
