# 2240. 자두나무
# Link: https://www.acmicpc.net/problem/2240
# Difficulty: Gold 5
# Category: 다이나믹 프로그래밍
from typing import List
import sys
input = sys.stdin.readline


# Solution 1: dynamic programming (3-dimensional)
# Time: 156 ms
# Memory: 40920 KB
class Solution1:
    def get_answer(self, t: int, w: int, tree: List[int]) -> int:
        data = [
            [(-sys.maxsize, -sys.maxsize) for _ in range(w + 1)] for _ in range(t)
        ]
        for i in range(t):
            data[i][0] = (
                sum(map(lambda x: x == 1, tree[:i + 1])), -sys.maxsize
            )
        data[0][1] = (-sys.maxsize, 1 if tree[0] == 2 else 0)
        for i in range(1, t):
            for j in range(1, w + 1):
                c1, c2 = data[i - 1][j - 1]
                p1, p2 = data[i - 1][j]
                t1 = 1 if tree[i] == 1 else 0
                t2 = 1 if tree[i] == 2 else 0
                data[i][j] = (max(c2, p1) + t1, max(c1, p2) + t2)
        return max(map(lambda x: max(x), data[-1]))


# Solution 2: dynamic programming (2-dimensional)
# Time: 156 ms
# Memory: 38840 KB
class Solution2:
    def get_answer(self, t: int, w: int, tree: List[int]) -> int:
        data = [[-sys.maxsize for _ in range(w + 1)] for _ in range(t)]
        for i in range(t):
            data[i][0] = (sum(map(lambda x: x == 1, tree[:i + 1])))
        data[0][1] = 1 if tree[0] == 2 else 0
        for i in range(1, t):
            for j in range(1, w + 1):
                move = data[i - 1][j - 1]
                stay = data[i - 1][j]
                current = tree[i] == j % 2 + 1
                data[i][j] = max(move, stay) + current
        return max(data[-1])


t, w = map(int, input().split())
tree = [int(input()) for _ in range(t)]
answer = Solution2().get_answer(t, w, tree)
print(answer)
