# 11054. 가장 긴 바이토닉 부분 수열
# Link: https://www.acmicpc.net/problem/11054
# Difficulty: Gold 4
# Category: 다이나믹 프로그래밍
from typing import List


# Solution 1: dynamic programming
# Time: 268 ms
# Memory: 38848 KB
class Solution:
    def get_answer(self, n: int, s: List[int]) -> int:
        def get_length(n: int, s: List[int]) -> List[int]:
            dp = [[0]]
            for idx in range(n):
                data = [*dp[-1]]
                for size in range(1, len(dp[-1])):
                    if s[idx] > dp[-1][size - 1]:
                        data[size] = min(data[size], s[idx])
                if s[idx] > dp[-1][-1]:
                    data.append(s[idx])
                dp.append(data)

            return list(map(lambda x: len(x) - 1, dp[1:]))

        inc = get_length(n, s)
        dec = get_length(n, s[::-1])[::-1]

        max_len = 0
        for t in range(n):
            max_len = max(max_len, inc[t] + dec[t] - 1)
        return max_len


n = int(input())
s = list(map(int, input().split()))
answer = Solution().get_answer(n, s)
print(answer)
