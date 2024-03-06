# 17070. 파이프 옮기기 1
# Link: https://www.acmicpc.net/problem/17070
# Difficulty: Gold 5
# Category: 다이나믹 프로그래밍
# Category: 그래프 이론
# Category: 그래프 탐색
from typing import List


# Solution 1: dynamic programming, memoization
# Time: 148 ms
# Memory: 39004 KB
class Solution:
    def get_answer(self, n: int, house: List[List[int]]) -> int:
        ways = [[[None for _ in range(3)] for _ in range(n)] for _ in range(n)]
        ways[0][0], ways[0][1] = [0, 0, 0], [1, 1, 0]

        def check_valid(x: int, y: int) -> bool:
            return 0 <= x < n and 0 <= y < n and house[x][y] == 0

        def get_ways(x: int, y: int, d: int) -> int:
            if ways[x][y][d] != None:
                return ways[x][y][d]

            res = 0
            if d in (0, 1) and check_valid(x, y - 1):
                res += get_ways(x, y - 1, 0)
            if d in (1, 2) and check_valid(x - 1, y):
                res += get_ways(x - 1, y, 2)
            if check_valid(x - 1, y - 1) and check_valid(x, y - 1) and check_valid(x - 1, y):
                res += get_ways(x - 1, y - 1, 1)
            ways[x][y][d] = res
            return res

        return get_ways(n - 1, n - 1, 1) if check_valid(n - 1, n - 1) else 0


n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
answer = Solution().get_answer(n, house)
print(answer)
