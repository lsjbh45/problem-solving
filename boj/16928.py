# 16928. 뱀과 사다리 게임
# Link: https://www.acmicpc.net/problem/16928
# Difficulty: Gold 5
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
from typing import List, Tuple
from collections import deque


# Solution 1: bfs
# Time: 148 ms
# Memory: 39048 KB
class Solution:
    def get_answer(self, ladders: List[Tuple[int, int]],
                   snakes: List[Tuple[int, int]]) -> int:
        ladder_dict = {x: y for x, y in ladders}
        snake_dict = {u: v for u, v in snakes}

        checked = [False for _ in range(101)]
        checked[1] = True

        q = deque()
        q.append((1, 0))

        while q:
            num, time = q.popleft()
            if num == 100:
                return time
            for d in range(1, 7):
                new = num + d
                if new > 100:
                    continue
                if new in ladder_dict:
                    new = ladder_dict[new]
                if new in snake_dict:
                    new = snake_dict[new]
                if checked[new]:
                    continue
                checked[new] = True
                q.append((new, time + 1))

        return -1


n, m = map(int, input().split())
ladders = [tuple(map(int, input().split())) for _ in range(n)]
snakes = [tuple(map(int, input().split())) for _ in range(m)]
answer = Solution().get_answer(ladders, snakes)
print(answer)
