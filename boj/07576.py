# 7576. 토마토
# Link: https://www.acmicpc.net/problem/7576
# Difficulty: Gold 5
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
from typing import List
from collections import deque
import sys
input = sys.stdin.readline


# Solution 1: bfs
# Time: 1296 ms
# Memory: 102120 KB
class Solution:
    directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    def get_answer(self, m: int, n: int, status: List[List[int]]):
        q = deque()
        for i in range(n):
            for j in range(m):
                if status[i][j] == 1:
                    q.append((i, j, 0))

        max_day = 0
        while q:
            i, j, day = q.popleft()
            for di, dj in self.directions:
                ni, nj, nday = i + di, j + dj, day + 1
                if not (0 <= ni < n and 0 <= nj < m):
                    continue
                if status[ni][nj] == 0:
                    status[ni][nj] = 1
                    max_day = max(max_day, nday)
                    q.append((ni, nj, nday))

        if any(any(tomato == 0 for tomato in row) for row in status):
            return -1
        return max_day


m, n = map(int, input().split())
status = [list(map(int, input().split())) for _ in range(n)]
answer = Solution().get_answer(m, n, status)
print(answer)
