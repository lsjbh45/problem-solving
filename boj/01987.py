# 1987. 알파벳
# Link: https://www.acmicpc.net/problem/1987
# Difficulty: Gold 4
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 깊이 우선 탐색
# Category: 백트래킹
from typing import List


# Solution 1: dfs, pruning, set
# Time: 1144 ms
# Memory: 59224 KB
class Solution:
    def get_answer(self, r: int, c: int, board: List[List[str]]) -> int:
        stack = set([(0, 0, board[0][0])])
        max_len = 0

        while stack:
            x, y, path = stack.pop()
            max_len = max(max_len, len(path))

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < r and 0 <= ny < c):
                    continue

                target = board[nx][ny]
                if target not in path:
                    stack.add((nx, ny, path + target))

        return max_len


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
answer = Solution().get_answer(r, c, board)
print(answer)
