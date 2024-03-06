# 01043. 거짓말
# Link: https://www.acmicpc.net/problem/1043
# Difficulty: Gold 4
# Category: 자료 구조
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 분리 집합
from typing import List


# Solution 1: disjoint set, floyd-warshall
# Time: 156 ms
# Memory: 38896 KB
class Solution:
    def get_answer(self, n: int, m: int, knows: List[int], parties: List[List[int]]) -> int:
        adj = [[i == j for i in range(n)] for j in range(n)]
        for party in parties:
            for i in range(len(party)):
                for j in range(i + 1, len(party)):
                    x, y = party[i] - 1, party[j] - 1
                    adj[x][y] = adj[y][x] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if adj[i][k] and adj[k][j]:
                        adj[i][j] = True

        ok = list(map(lambda p: all(
            not p[t] or t + 1 not in knows for t in range(n)
        ), adj))

        return sum(all(map(lambda t: ok[t - 1], party)) for party in parties)


n, m = map(int, input().split())
_, *knows = list(map(int, input().split()))
parties = []
for _ in range(m):
    _, *party = list(map(int, input().split()))
    parties.append(party)
answer = Solution().get_answer(n, m, knows, parties)
print(answer)
