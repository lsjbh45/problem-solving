# 4963. 섬의 개수
# Link: https://www.acmicpc.net/problem/4963
# Difficulty: Silver 2
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
# Category: 깊이 우선 탐색


# Soltion 1: dfs
# Time: 84 ms
# Memory: 31256 KB
def find_island_count(w, h, inst):
    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    def mark_island(x, y):
        check = [(x, y)]
        while check:
            x, y = check.pop()
            if inst[x][y]:
                inst[x][y] = 0
                for dx, dy in d:
                    if 0 <= x + dx < h and 0 <= y + dy < w:
                        check.append((x + dx, y + dy))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if inst[i][j]:
                cnt += 1
                mark_island(i, j)

    return cnt


w, h = map(int, input().split())

while w and h:
    inst = [list(map(int, input().split())) for _ in range(h)]
    cnt = find_island_count(w, h, inst)
    print(cnt)

    w, h = map(int, input().split())
