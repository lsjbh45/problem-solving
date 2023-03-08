# 1744. 수 묶기
# Link: https://www.acmicpc.net/problem/1744
# Difficulty: Gold 4
# Category: 그리디 알고리즘
# Category: 정렬
# Category: 많은 조건 분기
from typing import List


# Solution 1: divergence, greedy
# Time: 148 ms
# Memory: 37508 KB
class Solution:
    def get_max(self, n: int, nums: List[int]) -> int:
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        has_zero = any(num == 0 for num in nums)

        total = 0
        positive.sort(reverse=True)
        for nth in range(0, len(positive) // 2):
            if positive[nth * 2] == 1 or positive[nth * 2 + 1] == 1:
                total += positive[nth * 2] + positive[nth * 2 + 1]
            else:
                total += positive[nth * 2] * positive[nth * 2 + 1]
        if len(positive) % 2:
            total += positive[-1]

        negative.sort()
        for nth in range(0, len(negative) // 2):
            total += negative[nth * 2] * negative[nth * 2 + 1]
        if len(negative) % 2 and not has_zero:
            total += negative[-1]

        return total


n = int(input())
nums = [int(input()) for _ in range(n)]
answer = Solution().get_max(n, nums)
print(answer)
