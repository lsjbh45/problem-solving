# 14397. 해변
# Link: hhttps://www.acmicpc.net/problem/14397
# Difficulty: Silver 4
# Category: 구현
# Category: 그래프 이론
# Category: 그래프 탐색


# Solution 1: implementation
# Time: 288 ms
# Memory: 65240 KB
def get_search_list(n):
    return {(0, 1), (1, 0), [(1, -1), (1, 1)][n % 2]}


n, m = map(int, input().split())
map_ = [list(input()) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        for di, dj in get_search_list(i):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if map_[i][j] != map_[ni][nj]:
                    cnt += 1

print(cnt)
