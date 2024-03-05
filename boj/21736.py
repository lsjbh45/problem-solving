# 21736. 헌내기는 친구가 필요해
# Link: https://www.acmicpc.net/problem/21736
# Difficulty: Silver 2
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
# Category: 깊이 우선 탐색
from typing import List
from collections import deque


# Solution 1: bfs
# Time: 600 ms
# Memory: 54328 KB
class Solution:
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def get_answer(self, n: int, m: int, campus: List[List[str]]) -> int:
        q = deque()
        for i in range(n):
            for j in range(m):
                if campus[i][j] == 'I':
                    q.append((i, j))

        visited = [[False for _ in range(m)] for _ in range(n)]
        meet = 0

        while q:
            x, y = q.popleft()
            if campus[x][y] == 'X':
                continue
            if visited[x][y]:
                continue
            if campus[x][y] == 'P':
                meet += 1
            visited[x][y] = True

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if not 0 <= nx < n:
                    continue
                if not 0 <= ny < m:
                    continue
                q.append((nx, ny))

        return meet


n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]
answer = Solution().get_answer(n, m, campus)
print(answer if answer else 'TT')
