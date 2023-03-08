# 15654. N과 M (5)
# Link: https://www.acmicpc.net/problem/15654
# Difficulty: Silver 3
# Category: 백트래킹
from typing import List


# Solution 1: dfs
# Time: 312 ms
# Memory: 43968 KB
class Solution:
    def get_answer(self, n: int, m: int, nums: List[int]) -> List[List[int]]:
        def get_seq(seq: List[int], size: int) -> List[List[int]]:
            if not size:
                return [seq]

            result = []
            for k in [k for k in nums if k not in seq]:
                result += get_seq([*seq, k], size - 1)
            return result

        nums.sort()
        return get_seq([], m)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = Solution().get_answer(n, m, nums)
for sub in answer:
    print(' '.join(map(str, sub)))
