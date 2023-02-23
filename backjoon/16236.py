# 16236. 아기 상어
# Link: https://www.acmicpc.net/problem/16236
# Difficulty: Gold 3
# Category: 구현
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
# Category: 시뮬레이션
from typing import List, Tuple
import heapq


# Solution 1: implementation, bfs, priority queue
# Time: 156 ms
# Memory: 39892 KB
class Solution:
    directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    def get_answer(self, n: int, status: List[List[int]]):
        size, eat, time = 2, 0, 0

        def find_fish(shark: Tuple[int, int]):
            traversed = [[False for _ in range(n)] for _ in range(n)]
            pq = [(0, *shark)]
            while pq:
                t, x, y = heapq.heappop(pq)

                if 0 < status[x][y] < size:
                    return t, x, y

                if traversed[x][y]:
                    continue
                traversed[x][y] = True

                if status[x][y] > size:
                    continue

                for dx, dy in self.directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        heapq.heappush(pq, (t + 1, nx, ny))

            return None

        shark = (0, 0)
        for i in range(n):
            for j in range(n):
                if status[i][j] == 9:
                    shark = (i, j)
                    status[i][j] = 0

        while True:
            find = find_fish(shark)
            if not find:
                break

            t, x, y = find

            status[x][y] = 0
            time += t

            eat += 1
            if size == eat:
                size, eat = size + 1, 0

            shark = (x, y)

        return time


n = int(input())
status = [list(map(int, input().split())) for _ in range(n)]
answer = Solution().get_answer(n, status)
print(answer)
