# 3190. 뱀
# Link: https://www.acmicpc.net/problem/3190
# Difficulty: Gold 4
# Category: 구현
# Category: 자료 구조
# Category: 시뮬레이션
# Category: 덱
# Category: 큐
from typing import List, Tuple
from collections import deque


# Soltion 1: implementation
# Time: 156 ms
# Memory: 38952 KB
class Solution:
    movement = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def __init__(self):
        self.board = [[0 for _ in range(102)] for _ in range(102)]

        self.indices = deque([(1, 1)])
        self.head = (1, 1)
        self.board[1][1] = 3

        self.direction = 0
        self.time = 0

    def rotate(self, rotation: str):
        self.direction = (self.direction + (-1 if rotation == 'L' else 1)) % 4

    def start(self, n: int, apples: List[Tuple[int, int]]) -> None:
        for c, r in apples:
            self.board[r][c] = 1
        for i in range(n + 1):
            self.board[0][i] = 2
            self.board[n + 1][i] = 2
            self.board[i][0] = 2
            self.board[i][n + 1] = 2

    def move(self) -> bool:
        x, y = self.head
        dx, dy = self.movement[self.direction]
        nx, ny = x + dx, y + dy

        if self.board[nx][ny] == 2 or self.board[nx][ny] == 3:
            return True

        if self.board[x + dx][y + dy] == 0:
            ix, iy = self.indices.popleft()
            self.board[ix][iy] = 0

        self.head = (nx, ny)
        self.indices.append((nx, ny))
        self.board[nx][ny] = 3

    def get_answer(self, n: int, apples: List[Tuple[int, int]], rotations: List[Tuple[int, str]]) -> int:
        self.start(n, apples)

        rotation_idx = 0
        while True:
            self.time += 1
            if self.move():
                return self.time
            if rotation_idx < len(rotations):
                x, c = rotations[rotation_idx]
                if self.time == x:
                    self.rotate(c)
                    rotation_idx += 1


n = int(input())
k = int(input())
apples = [tuple(map(int, input().split())) for _ in range(k)]
l = int(input())
rotations = [(int(x), c) for x, c in [input().split() for _ in range(l)]]
answer = Solution().get_answer(n, apples, rotations)
print(answer)
