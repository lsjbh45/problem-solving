# 1976. 여행 가자
# Link: https://www.acmicpc.net/problem/1976
# Difficulty: Gold 4
# Category: 자료 구조
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 분리 집합
from typing import List


# Solution 1: union-find
# Time: 156 ms
# Memory: 38864 KB
class Solution:
    class UnionFind:
        def __init__(self, n: int):
            self.parent = [i for i in range(n)]

        def find(self, x: int) -> int:
            if x == self.parent[x]:
                return x

            return self.find(self.parent[x])

        def union(self, x: int, y: int) -> None:
            rx = self.find(x)
            ry = self.find(y)

            self.parent[ry] = rx

    def get_answer(self, n: int, m: int, conn: List[List[int]], trip: int) -> bool:
        uf = self.UnionFind(n)
        for i in range(n):
            for j in range(n):
                if conn[i][j] == 1:
                    uf.union(i, j)

        for x, y in ((trip[i] - 1, trip[i + 1] - 1) for i in range(m - 1)):
            if uf.find(x) != uf.find(y):
                return False

        return True


n = int(input())
m = int(input())
conn = [list(map(int, input().split())) for _ in range(n)]
trip = list(map(int, input().split()))
answer = Solution().get_answer(n, m, conn, trip)
print('YES' if answer else 'NO')
