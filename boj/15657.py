# 15657. N과 M (8)
# Link: https://www.acmicpc.net/problem/15657
# Difficulty: Silver 3
# Category: 백트래킹
from typing import List


# Solution 1: dfs
# Time: 156 ms
# Memory: 38892 KB
class Solution:
    def get_answer(self, n: int, m: int, nums: List[int]) -> List[List[int]]:
        def get_subseq(start: int, size: int) -> List[List[int]]:
            if size == 1:
                return [[nums[k]] for k in range(start, n)]

            answer = []
            for k in range(start, n):
                subseq = get_subseq(k, size - 1)
                answer += [[nums[k], *seq] for seq in subseq]
            return answer

        nums.sort()
        return get_subseq(0, m)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = Solution().get_answer(n, m, nums)
for sub in answer:
    print(' '.join(map(str, sub)))
