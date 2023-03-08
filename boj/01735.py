# 1735. 분수 합
# Link: https://www.acmicpc.net/problem/1735
# Difficulty: Silver 3
# Category: 수학
# Category: 정수론
# Category: 유클리드 호제법
from typing import Tuple


# Solution 1: math
# Time: 144 ms
# Memory: 38864 KB
class Solution:
    def gcd(self, a: int, b: int):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def get_frac(self, a1: int, b1: int, a2: int, b2: int) -> Tuple[int, int]:
        a, b = a1 * b2 + b1 * a2, b1 * b2
        gcd = self.gcd(a, b)
        return (a // gcd, b // gcd)


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
answer = Solution().get_frac(a1, b1, a2, b2)
print(*answer)
