# 2251. 물통
# Link: https://www.acmicpc.net/problem/2251
# Difficulty: Gold 5
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 너비 우선 탐색
# Category: 깊이 우선 탐색
from typing import List, Tuple
from collections import deque


# Solution 1: dfs, implementation
# Time: 136 ms
# Memory: 38904 KB
class Solution:
    def get_answer(self, a: int, b: int, c: int) -> List[int]:
        q = deque([(0, 0, c)])
        checked = set()
        found = set()

        def pour(t: int, s: int, tm: int) -> Tuple[int, int]:
            if t + s <= tm:
                return t + s, 0
            return tm, t + s - tm

        while q:
            ca, cb, cc = q.popleft()
            if (ca, cb) in checked:
                continue

            if ca == 0:
                found.add(cc)
            checked.add((ca, cb))

            if 0 <= ca < a:
                na, nb, nc = (*pour(ca, cb, a), cc)
                q.append((na, nb, nc))
                na, nc, nb = (*pour(ca, cc, a), cb)
                q.append((na, nb, nc))
            if 0 <= cb < b:
                nb, na, nc = (*pour(cb, ca, b), cc)
                q.append((na, nb, nc))
                nb, nc, na = (*pour(cb, cc, b), ca)
                q.append((na, nb, nc))
            if 0 <= cc < c:
                nc, na, nb = (*pour(cc, ca, c), cb)
                q.append((na, nb, nc))
                nc, nb, na = (*pour(cc, cb, c), ca)
                q.append((na, nb, nc))

        return sorted(found)


a, b, c = map(int, input().split())
answer = Solution().get_answer(a, b, c)
print(' '.join(map(str, answer)))
