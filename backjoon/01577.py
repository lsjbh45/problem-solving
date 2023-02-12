# 1577. 도로의 개수
# Link: https://www.acmicpc.net/problem/1577
# Difficulty: Gold 5
# Category: 다이나믹 프로그래밍


# Soltion 1: dynamic programming, tabulation
# Time: 52 ms
# Memory: 32276 KB
n, m = map(int, input().split())
k = int(input())

paths = [tuple(map(int, input().split())) for _ in range(k)]

pos = [[[True, True] for _ in range(m + 1)] for _ in range(n + 1)]
for x1, y1, x2, y2 in paths:
    if x1 > x2 or y1 > y2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    pos[x2][y2][x1 == x2] = False

cases = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        if not i and not j:
            cases[i][j] = 1
            continue
        posx, posy = pos[i][j]
        if i > 0 and posx:
            cases[i][j] += cases[i - 1][j]
        if j > 0 and posy:
            cases[i][j] += cases[i][j - 1]

print(cases[-1][-1])
