# 14940. 쉬운 최단거리
# Link: https://www.acmicpc.net/problem/14940
# Difficulty: Silver 1
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
from typing import List
from collections import deque


# Solution 1: bfs
# Time: 592 ms
# Memory: 43496 KB
class Solution:
    def get_answer(self, n: int, m: int, mp: List[List[int]]) -> List[List[int | None]]:
        result = list(
            map(lambda r: list(map(lambda e: -1 if e else 0, r)), mp))
        q = deque([])

        for i in range(n):
            for j in range(m):
                if mp[i][j] == 2:
                    q.append((0, i, j))

        while q:
            dst, x, y = q.popleft()
            if result[x][y] != -1:
                continue
            result[x][y] = dst

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if not 0 <= nx < n:
                    continue
                if not 0 <= ny < m:
                    continue
                if mp[nx][ny] == 0:
                    continue
                q.append((dst + 1, nx, ny))

        return result


n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
answer = Solution().get_answer(n, m, mp)
for sub in answer:
    print(' '.join(map(lambda e: str(e) if e != None else '0', sub)))
