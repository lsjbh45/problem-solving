# 7569. 토마토
# Link: https://www.acmicpc.net/problem/7569
# Difficulty: Gold 5
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색


# Solution 1: bfs
# Time: 4156 ms
# Memory: 50544 KB
from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
status = [
    [list(map(int, input().split())) for _ in range(n)] for _ in range(h)
]

q = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if status[i][j][k] == 1:
                q.append((i, j, k, 0))

max_day = 0
directions = {
    (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)
}
while q:
    i, j, k, day = q.popleft()
    for di, dj, dk in directions:
        ni, nj, nk, nday = i + di, j + dj, k + dk, day + 1
        if not (0 <= ni < h and 0 <= nj < n and 0 <= nk < m):
            continue
        if status[ni][nj][nk] == 0:
            status[ni][nj][nk] = 1
            max_day = max(max_day, nday)
            q.append((ni, nj, nk, nday))

if any(any(any(x == 0 for x in y) for y in z) for z in status):
    print(-1)
else:
    print(max_day)
