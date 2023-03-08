# 14503. 로봇 청소기
# Link: https://www.acmicpc.net/problem/14503
# Difficulty: Gold 5
# Category: 구현
# Category: 시뮬레이션
from typing import List


# Solution 1: implementation
# Time: 140 ms
# Memory: 38924 KB
class Solution:
    direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

    def get_cnt(self, n: int, m: int, r: int, c: int, d: int,
                status: List[List[int]]) -> int:
        cnt = 0
        while True:
            if status[r][c] == 0:
                status[r][c] = 2
                cnt += 1
            if all(
                status[r + dx][c + dy] != 0
                for dx, dy in self.direction.values()
            ):
                dx, dy = self.direction[(d + 2) % 4]
                if status[r + dx][c + dy] == 2:
                    r, c = r + dx, c + dy
                    continue
                else:
                    break
            else:
                d = (d - 1) % 4
                dx, dy = self.direction[d]
                while status[r + dx][c + dy] != 0:
                    d = (d - 1) % 4
                    dx, dy = self.direction[d]
                r, c = r + dx, c + dy

        return cnt


n, m = map(int, input().split())
r, c, d = map(int, input().split())
status = [list(map(int, input().split())) for _ in range(n)]
answer = Solution().get_cnt(n, m, r, c, d, status)
print(answer)
