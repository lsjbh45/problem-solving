# 13549. 숨바꼭질 3
# Link: https://www.acmicpc.net/problem/13549
# Difficulty: Gold 5
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
# Category: 데이크스트라
# Category: 최단 경로
# Category: 0-1 너비 우선 탐색
from collections import deque
import heapq


# Soltion 1: bfs
# Time: 228 ms
# Memory: 54592 KB
class Solution1():
    def get_answer(self, n: int, k: int) -> int:
        def get_squares(n):
            if n == 0:
                return [0]

            lst = []
            while n <= 100000:
                lst.append(n)
                n = 2 * n
            return lst

        def get_moves(n):
            lst = []
            if n >= 1:
                lst.append(n - 1)
            if n <= 99999:
                lst.append(n + 1)
            return lst

        q = deque()
        check = [False for _ in range(100001)]

        for square in get_squares(n):
            q.append((square, 0))

        while True:
            n, s = q.popleft()
            if n == k:
                return s
            check[n] = True

            for move in get_moves(n):
                if check[move]:
                    continue
                for square in get_squares(move):
                    if check[square]:
                        continue
                    q.append((square, s + 1))


# Soltion 2: priority queue
# Time: 232 ms
# Memory: 39584 KB
class Solution2():
    def get_answer(self, n: int, k: int) -> int:
        q = []
        heapq.heappush(q, (0, n))

        check = [False for _ in range(100001)]

        while q:
            s, n = heapq.heappop(q)
            if n == k:
                return s
            check[n] = True

            for s, n in ((s + 1, n - 1), (s + 1, n + 1), (s, n * 2)):
                if n < 0 or n > 100000 or check[n]:
                    continue
                heapq.heappush(q, (s, n))


n, k = map(int, input().split())
answer = Solution2().get_answer(n, k)
print(answer)
