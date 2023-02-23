# 1802. 종이 접기
# Link: https://www.acmicpc.net/problem/1802
# Difficulty: Silver 1
# Category: 애드 혹
# Category: 분할 정복
from typing import List


# Solution 1: implementation
# Time: 148 ms
# Memory: 38864 KB
class Solution:
    def get_possibility(self, fold: List[str]) -> bool:
        step = 2
        while step < len(fold):
            start = step // 2 - 1
            direction = '1' if fold[start] == '0' else '0'
            for pos in range(start, len(fold), step):
                if fold[pos] == direction:
                    return False
                direction = fold[pos]
            step *= 2
        return True


t = int(input())
for _ in range(t):
    fold = list(input())
    possibility = Solution().get_possibility(fold)
    print('YES' if possibility else 'NO')
