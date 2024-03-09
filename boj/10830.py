# 10830. 행렬 제곱
# Link: https://www.acmicpc.net/problem/10830
# Difficulty: Gold 4
# Category: 수학
# Category: 분할 정복
# Category: 분할 정복을 이용한 거듭제곱
# Category: 선형대수학
from typing import List


# Solution 1: divide and conquer
# Time: 148 ms
# Memory: 38836 MB
class Solution:
    def get_answer(self, n: int, b: int, matrix: List[List[int]]) -> List[List[int]]:
        matrix = list(map(lambda c: list(map(lambda e: e % 1000, c)), matrix))

        def mat_mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            return [
                [
                    sum([a[i][k] * b[k][j] for k in range(n)]) % 1000
                    for j in range(n)
                ]
                for i in range(n)
            ]

        def get_kth(k: int) -> List[List[int]]:
            if k == 1:
                return matrix

            h = get_kth(k // 2)
            if k % 2 == 0:
                return mat_mul(h, h)
            else:
                return mat_mul(mat_mul(h, h), matrix)

        return get_kth(b)


n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = Solution().get_answer(n, b, matrix)

for row in answer:
    print(' '.join(map(str, row)))
