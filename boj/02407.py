# 2407. 조합
# Link: https://www.acmicpc.net/problem/2407
# Difficulty: Silver 3
# Category: 수학
# Category: 조합론
# Category: 임의 정밀도 / 큰 수 연산


#  Solution 1: math, dynamic programming
# Time: 52 ms
# Memory: 31256 ms
class Solution:
    combinations = {}

    def combination(self, n: int, m: int) -> int:
        if (n, m) in self.combinations:
            return self.combinations[(n, m)]
        if m == 0 or m == n:
            result = 1
        else:
            result = self.combination(n - 1, m - 1) + \
                self.combination(n - 1, m)
        self.combinations[(n, m)] = result
        return result


n, m = map(int, input().split())
result = Solution().combination(n, m)
print(result)
