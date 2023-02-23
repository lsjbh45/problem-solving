# 9019. DSLR
# Link: https://www.acmicpc.net/problem/9019
# Difficulty: Gold 4
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
from typing import Tuple, List
from collections import deque


# Solution 1: bfs, dynamic programming
# Time: 10644 ms
# Memory: 225552 KB
class Solution:
    def get_answer(self, a: int, b: int) -> str:
        checked: List[bool] = [False for _ in range(10000)]
        q: deque[Tuple[int, str]] = deque([(a, '')])

        cnt = 0
        while q:
            cnt += 1
            n, x = q.popleft()

            if n == b:
                return x

            if checked[n]:
                continue
            checked[n] = True

            q.append(((n * 2) % 10000, x + 'D'))
            q.append(((n - 1) % 10000, x + 'S'))
            q.append(((n % 1000) * 10 + n // 1000, x + 'L'))
            q.append(((n % 10) * 1000 + n // 10, x + 'R'))

        return ''


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    answer = Solution().get_answer(a, b)
    print(answer)
