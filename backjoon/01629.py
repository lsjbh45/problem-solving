# 1629. 곱셈
# Link: https://www.acmicpc.net/problem/1629
# Difficulty: Silver 1
# Category: 수학
# Category: 분할 정복을 이용한 거듭제곱

# Solution 1: math
# Time: 40 ms
# Memory: 31256 KB
class Solution:
    def get_exp_mod(self, a: int, b: int, c: int) -> int:
        if b == 1:
            return a % c
        if b % 2:
            return (self.get_exp_mod(a, b - 1, c) * a) % c
        return (self.get_exp_mod(a, b // 2, c) ** 2) % c


a, b, c = map(int, input().split())
answer = Solution().get_exp_mod(a, b, c)
print(answer)
