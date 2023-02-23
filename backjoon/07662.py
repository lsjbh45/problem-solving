# 7662. 이중 우선순위 큐
# Link: https://www.acmicpc.net/problem/7662
# Difficulty: Gold 4
# Category: 자료 구조
# Category: 트리를 사용한 집합과 맵
# Category: 우선순위 큐
from typing import List, Tuple
import heapq
import sys
input = sys.stdin.readline


# Solution 1: priority queue
# Time: 9548 ms
# Memory: 484700 KB
class Solution:
    def get_answer(self, operations: List[Tuple[str, int]]) \
            -> Tuple[int, int] | None:
        min_heap = []
        max_heap = []
        deleted = [True]
        k = 1

        for op, n in operations:
            if op == 'I':
                heapq.heappush(min_heap, (n, k))
                heapq.heappush(max_heap, (-n, k))
                deleted.append(False)
                k = k + 1
            else:
                idx = 0
                if n == -1:
                    while min_heap and deleted[idx]:
                        _, idx = heapq.heappop(min_heap)
                else:
                    while max_heap and deleted[idx]:
                        _, idx = heapq.heappop(max_heap)
                deleted[idx] = True

        min_val, idx = 0, 0
        while deleted[idx]:
            if not min_heap:
                return None
            min_val, idx = heapq.heappop(min_heap)

        max_val, idx = 0, 0
        while deleted[idx]:
            if not max_heap:
                return None
            max_val, idx = heapq.heappop(max_heap)

        return -max_val, min_val


t = int(input())
for _ in range(t):
    k = int(input())
    operations = [
        (op, int(n)) for op, n in [input().split() for _ in range(k)]
    ]
    answer = Solution().get_answer(operations)
    print(' '.join(map(str, answer)) if answer is not None else 'EMPTY')
