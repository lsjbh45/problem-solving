# 12851.
# Link: https://www.acmicpc.net/problem/12851
# Difficulty: Gold 4
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
from typing import Tuple
from collections import deque
from sys import maxsize


# Solution 1: bfs, pruning
# Time: 280 ms
# Memory: 57792 KB
class Solution:
    def get_answer(self, n: int, m: int) -> Tuple[int, int]:
        q = deque([(0, n)])
        visited = {}

        min_t = maxsize
        m_num = 0

        while q:
            t, pos = q.popleft()

            if t > min_t:
                return min_t, m_num

            if pos == k:
                min_t = t
                m_num += 1

            if pos in visited and visited[pos] < t:
                continue
            visited[pos] = t

            for new_pos in (pos - 1, pos + 1, pos * 2):
                if 0 <= new_pos <= 100000:
                    q.append((t + 1, new_pos))


n, k = map(int, input().split())
t, m = Solution().get_answer(n, k)
print(t, m, sep='\n')
