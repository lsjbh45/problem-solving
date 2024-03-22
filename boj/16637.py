# 16637. 자두나무
# Link: https://www.acmicpc.net/problem/16637
# Difficulty: Gold 3
# Category: 구현
# Category: 브루트포스 알고리즘
from collections import deque
from typing import List
import sys


# Solution 1: implementation
# Time: 152 ms
# Memory: 37752 KB
class Solution1:
    def get_answer(self, n: int, expr: str) -> int:
        def op2(x: int | str, y: int | str, op: str) -> int:
            x, y = int(x), int(y)
            return x + y if op == '+' else x * y if op == '*' else x - y

        def calculate(cal: List[int | str]) -> int:
            if len(cal) == 1:
                return int(cal[0])
            if len(cal) == 3:
                return op2(cal[0], cal[2], cal[1])
            return calculate([op2(cal[0], cal[2], cal[1]), *cal[3:]])

        lst = []
        q = deque([])
        q.append(([], list(expr)))
        while q:
            e1, e2 = q.popleft()
            if len(e2) == 1:
                lst.append([*e1, *e2])
                continue
            if len(e2) == 3:
                lst.append([*e1, *e2])
                lst.append([*e1, op2(e2[0], e2[2], e2[1])])
                continue
            q.append(([*e1, *e2[0:2]], e2[2:]))
            q.append(([*e1, op2(e2[0], e2[2], e2[1]), e2[3]], e2[4:]))

        smax = -sys.maxsize
        for cal in lst:
            smax = max(smax, calculate(cal))
        return smax


# Solution 2: implementation
# Time: 160 ms
# Memory: 37784 KB
class Solution2:
    def get_answer(self, n: int, expr: str) -> int:
        def eval_2(x: int, y: int, op: str) -> int:
            return x + y if op == '+' else x * y if op == '*' else x - y

        q = deque()
        q.append(([], n // 2))
        seq = []

        while q:
            group, left = q.popleft()
            if left == 0:
                seq.append(group)
                continue
            q.append(([*group, False], left - 1))
            if len(group) == 0 or not group[-1]:
                q.append(([*group, True], left - 1))

        s_max = -sys.maxsize
        for group in seq:
            nums = list(map(int, expr[::2][::-1]))
            ops = list(expr[1::2][::-1])
            acc = (0, '+')
            while len(nums) > 0:
                if len(group) > 0 and group.pop() == 1:
                    op = ops.pop()
                    x, y = nums.pop(), nums.pop()
                    ty = eval_2(x, y, op)
                    if len(group) > 0:
                        group.pop()
                else:
                    ty = nums.pop()
                tx, top = acc
                tz = eval_2(tx, ty, top)
                acc = (tz, ops.pop() if len(ops) > 0 else '')
            res, _ = acc
            s_max = max(s_max, res)

        return s_max


n = int(input())
expr = input()
answer = Solution2().get_answer(n, expr)
print(answer)
