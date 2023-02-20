# 15663. N과 M (9)
# Link: https://www.acmicpc.net/problem/15663
# Difficulty: Silver 2
# Category: 백트래킹
from typing import List


# Solution 1: dfs
# Time: 232 ms
# Memory: 40940 KB
class Solution:
    def get_answer(self, n: int, m: int, nums: List[int]) -> List[List[int]]:
        def get_seq(lst: List[int], size: int) -> List[List[int]]:
            if not size:
                return []

            prev = 0
            seq = []
            for idx, num in enumerate(lst):
                if num != prev:
                    prev = num
                    sub = get_seq(lst[:idx] + lst[idx + 1:], size - 1)
                    seq += [[num, *each] for each in sub] if sub else [[num]]
            return seq

        nums.sort()
        return get_seq(nums, m)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = Solution().get_answer(n, m, nums)
for each in answer:
    print(*each)
