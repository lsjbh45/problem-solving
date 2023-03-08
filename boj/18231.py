# 18231. 파괴된 도시
# Link: https://www.acmicpc.net/problem/18231
# Difficulty: Gold 5
# Category: 그래프 이론
# Category: 그리디 알고리즘
# Category: 그래프 탐색


# Solution 1: graph, greedy
# Time: 288 ms
# Memory: 65240 KB
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = {tuple(map(int, input().split())) for _ in range(m)}
k = int(input())
destroyed = set(map(int, input().split()))

is_destroyed = {v: v in destroyed for v in range(1, n + 1)}
adj = {v: set() for v in range(1, n + 1)}
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)

checked = set()
bomb = set()
for v in range(1, n + 1):
    if is_destroyed[v] and all(is_destroyed[u] for u in adj[v]):
        bomb.add(v)
        checked.add(v)
        checked.update(adj[v])

if destroyed == checked:
    print(len(bomb))
    print(' '.join(map(str, bomb)))
else:
    print(-1)
