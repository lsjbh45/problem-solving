# 15666. N과 M (12)
# Link: https://www.acmicpc.net/problem/15666
# Difficulty: Silver 2
# Category: 백트래킹
from typing import List


# Solution 1: dfs
# Time: 156 ms
# Memory: 38836 KB
class Solution:
    def get_answer(self, n: int, m: int, nums: List[int]) -> List[List[int]]:
        def get_seq(start: int, size: int) -> List[List[int]]:
            if not size:
                return [[]]
            return sum([[
                [unique[k], *seq] for seq in get_seq(k, size - 1)
            ] for k in range(start, total)], [])

        unique = sorted(set(nums))
        total = len(unique)
        return get_seq(0, m)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = Solution().get_answer(n, m, nums)
for each in answer:
    print(*each)
