# 17392. 우울한 방학
# Link: hhttps://www.acmicpc.net/problem/17392
# Difficulty: Silver 1
# Category: 수학
# Category: 그리디 알고리즘
from typing import List
from collections import deque


# Solution 1: greedy
# Time: 72 ms (O(n))
# Memory: 34140 KB
class Solution1:
    def get_answer(self, n: int, m: int, h_list: List[int]) -> int:
        mood_list = [-1]
        for h in h_list:
            while h >= 0:
                m -= 1
                h -= 1
            mood_list.append(h)

        mood_list = deque(sorted(mood_list, reverse=True))

        total = 0
        while m > 0:
            mood = mood_list.popleft()
            total += mood ** 2

            m -= 1
            mood -= 1

            mood_list.append(mood)

        return total


# Solution 2: greedy, math
# Time: 152 ms
# Memory: 38876 KB
class Solution2:
    def sum_of_square(self, n: int) -> int:
        return n * (n + 1) * (2 * n + 1) // 6

    def get_answer(self, n: int, m: int, h_list: List[int]) -> int:
        day = m - sum(h + 1 for h in h_list)
        if day < 0:
            return 0

        cont, cnt = day // (n + 1), day % (n + 1)
        return ((n + 1) - cnt) * self.sum_of_square(cont) \
            + cnt * self.sum_of_square(cont + 1)


n, m = map(int, input().split())
h_list = list(map(int, input().split()))
answer = Solution2().get_answer(n, m, h_list)
print(answer)
