# 16953. A → B
# Link: https://www.acmicpc.net/problem/16953
# Difficulty: Silver 2
# Category: 그래프 이론
# Category: 그리디 알고리즘
# Category: 그래프 탐색
# Category: 너비 우선 탐색
from collections import deque


# Solution 1: bfs
# Time: 100 ms
# Memory: 34128 KB
class Solution:
    def get_answer(self, a: int, b: int) -> int:
        if a == b:
            return 1
        if a > b:
            return -1

        q = deque()
        q.append((a, 1))

        while q:
            num, cnt = q.popleft()
            for new in (num * 2, int(str(num) + '1')):
                if new == b:
                    return cnt + 1
                if new < b:
                    q.append((new, cnt + 1))

        return -1


a, b = map(int, input().split())
answer = Solution().get_answer(a, b)
print(answer)
