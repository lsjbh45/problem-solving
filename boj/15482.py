# 15482. 한글 LCS
# Link: hhttps://www.acmicpc.net/problem/15482
# Difficulty: Gold 5
# Category: 구현
# Category: 다이나믹 프로그래밍
# Category: 문자열
# Category: 파싱
# Category: utf-8 입력 처리
from typing import List
import sys
sys.setrecursionlimit(10 ** 6)


# Solution 1: memoization
# Time: 1780 ms
# Memory: 48500 KB
class Solution1:
    def get_answer(self, l1: str, l2: str) -> int:
        dp: List[List[int]] = [
            [-1 for _ in range(len(l2))] for _ in range(len(l1))
        ]

        def get_lcs(i1: int, i2: int) -> int:
            if i1 >= len(l1) or i2 >= len(l2):
                return 0
            if dp[i1][i2] != -1:
                return dp[i1][i2]

            lcs = get_lcs(i1 + 1, i2)

            if l1[i1] in l2[i2:]:
                l2_idx = l2.index(l1[i1], i2)
                lcs_c = get_lcs(i1 + 1, l2_idx + 1) + 1
                lcs = max(lcs, lcs_c)

            dp[i1][i2] = lcs
            return lcs

        return get_lcs(0, 0)


# Solution 2: tabulation
# Time: 568 ms
# Memory: 43888 KB
class Solution2:
    def get_answer(self, l1: str, l2: str) -> int:
        dp: List[List[int]] = [
            [-1 for _ in range(len(l2) + 1)] for _ in range(len(l1) + 1)
        ]

        for i in range(len(l1) + 1):
            for j in range(len(l2) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    continue

                if l1[i - 1] == l2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(l1)][len(l2)]


l1 = input()
l2 = input()
answer = Solution2().get_answer(l1, l2)
print(answer)
