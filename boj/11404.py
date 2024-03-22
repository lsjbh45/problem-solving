# 11404. 플로이드
# Link: https://www.acmicpc.net/problem/11404
# Difficulty: Gold 4
# Category: 그래프 이론
# Category: 최단 경로
# Category: 플로이드–워셜
from typing import List
from sys import maxsize


# Solution 1: floyd-warshall
# Time: 4304 ms
# Memory: 54196 KB
class Solution:
    def get_answer(self, n: int, m: int, buses: List[List[int]]) -> List[List[int]]:
        cost = [[0 if i == j else maxsize for j in range(n)] for i in range(n)]

        for a, b, c in buses:
            cost[a - 1][b - 1] = min(cost[a - 1][b - 1], c)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

        return cost


n = int(input())
m = int(input())
buses = [list(map(int, input().split())) for _ in range(m)]
answer = Solution().get_answer(n, m, buses)
for row in answer:
    print(' '.join(map(lambda x: str(x) if x != maxsize else '0', row)))
