# 15686. 이진 검색 트리
# Link: https://www.acmicpc.net/problem/15686
# Difficulty: Gold 5
# Category: 구현
# Category: 브루트포스 알고리즘
# Category: 백트래킹
from typing import List
from itertools import combinations


# Solution 1: brute-forces
# Time: 284 ms
# Memory: 38852 KB
class Solution:
    def get_answer(self, n: int, m: int, city: List[List[int]]) -> int:
        homes, chickens = [], []
        for i in range(n):
            for j in range(n):
                if city[i][j] == 1:
                    homes.append((i, j))
                if city[i][j] == 2:
                    chickens.append((i, j))

        dists = [list(map(
            lambda c: abs(c[0] - hx) + abs(c[1] - hy), chickens
        )) for hx, hy in homes]

        selections = combinations(range(len(chickens)), m)
        return min(
            sum(
                min(
                    dist[chicken] for chicken in selection
                ) for dist in dists
            ) for selection in selections
        )


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
answer = Solution().get_answer(n, m, city)
print(answer)
