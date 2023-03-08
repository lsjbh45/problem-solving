# 2418. 단어 격자
# Link: https://www.acmicpc.net/problem/2418
# Difficulty: Gold 5
# Category: 구현
# Category: 다이나믹 프로그래밍
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색


# Solution 1: dynamic programming, tabulation
# Time: 120 ms
# Memory: 31384 KB
h, w, _ = map(int, input().split())

grid = [list(input()) for _ in range(h)]

word = input()

cnt = [[1 if grid[i][j] == word[-1]
        else 0 for j in range(w)] for i in range(h)]

cases = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

for char in word[::-1][1:]:
    result = [[0 for _ in range(w)] for _ in range(h)]
    for x in range(h):
        for y in range(w):
            if char == grid[x][y]:
                for dx, dy in cases:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w:
                        result[x][y] += cnt[nx][ny]
    cnt = result

print(sum(map(sum, cnt)))
