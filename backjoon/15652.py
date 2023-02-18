# 15652. N과 M (4)
# Link: https://www.acmicpc.net/problem/15652
# Difficulty: Silver 3
# Category: 백트래킹
from typing import List


# Solution 1: dfs
# Time: 164 ms
# Memory: 38444 KB
class Solution:
    def get_answer(self, n: int, m: int) -> List[List[int]]:
        def get_subseq(start: int, size: int) -> List[List[int]]:
            if size == 1:
                return [[k] for k in range(start, n + 1)]

            answer = []
            for k in range(start, n + 1):
                subseq = get_subseq(k, size - 1)
                answer += [[k, *seq] for seq in subseq]
            return answer

        return get_subseq(1, m)


n, m = map(int, input().split())
answer = Solution().get_answer(n, m)
for sub in answer:
    print(' '.join(map(str, sub)))
