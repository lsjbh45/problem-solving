# 1697. 숨바꼭질
# Link: https://www.acmicpc.net/problem/1697
# Difficulty: Silver 1
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
from collections import deque


# Solution 1: bfs
# Time: 100 ms
# Memory: 34376 KB
class Solution:
    def get_answer(self, x: int, k: int) -> int:
        checked = [False for _ in range(100001)]
        checked[x] = True

        q = deque()
        q.append((x, 0))

        while q:
            pos, time = q.popleft()
            if pos == k:
                return time
            for move in (pos + 1, pos - 1, 2 * pos):
                if 0 <= move <= 100000:
                    if not checked[move]:
                        q.append((move, time + 1))
                        checked[move] = True

        return -1


x, k = map(int, input().split())
answer = Solution().get_answer(x, k)
print(answer)
