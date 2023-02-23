# 9251. LCS
# Link: https://www.acmicpc.net/problem/9251
# Difficulty: Gold 5
# Category: 다이나믹 프로그래밍
# Category: 문자열


# Solution 1: dynamic programming
# Time: 376 ms
# Memory: 56452 KB
class Solution:
    def get_answer(self, s1: str, s2: str) -> int:
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]


s1 = input()
s2 = input()
answer = Solution().get_answer(s1, s2)
print(answer)
