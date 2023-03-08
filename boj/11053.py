# 11053. 가장 긴 증가하는 부분 수열
# Link: https://www.acmicpc.net/problem/11053
# Difficulty: Silver 2
# Category: 다이나믹 프로그래밍
from typing import List
import heapq


# Solution 1: priority queue
# Time: 288 ms
# Memory: 40920 KB
class Solution1:
    def get_answer(self, n: int, A: List[int]) -> int:
        pq = []
        heapq.heappush(pq, (0, 0))

        for a in A:
            length, highest = heapq.heappop(pq)
            peek_list = [(length, highest)]
            while highest >= a:
                length, highest = heapq.heappop(pq)
                peek_list.append((length, highest))
            heapq.heappush(pq, (length - 1, a))
            for peek in peek_list:
                heapq.heappush(pq, peek)

        return -heapq.heappop(pq)[0]


# Solution 2: dynamic programming
# Time: 160 ms
# Memory: 38820 KB
class Solution2:
    def get_answer(self, n: int, A: List[int]) -> int:
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = max([dp[j] for j in range(i) if A[j] < A[i]] or [0]) + 1
        return max(dp)


n = int(input())
A = list(map(int, input().split()))
answer = Solution2().get_answer(n, A)
print(answer)
