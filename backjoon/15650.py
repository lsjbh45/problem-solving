# 15650. N과 M (2)
# Link: https://www.acmicpc.net/problem/15650
# Difficulty: Silver 3
# Category: 백트래킹
from typing import List


# Solution 1: dfs, backtracking
# Time: 152 ms
# Memory: 38836 KB
class Solution:
    def get_answer(self, n: int, m: int) -> List[List[int]]:
        def get_seq(start: int, size: int) -> List[List[int]]:
            if size == 1:
                return [[k] for k in range(start, n + 1)]
            if n - start + 1 < size:
                return []
            result = sum([
                [[k, *seq] for seq in get_seq(k + 1, size - 1)]
                for k in range(start, n + 1)
            ], [])
            return result

        return get_seq(1, m)


n, m = map(int, input().split())
answer = Solution().get_answer(n, m)
for sub in answer:
    print(' '.join(map(str, sub)))
