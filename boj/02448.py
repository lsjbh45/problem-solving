# 2448, 별 찍기 - 11
# Link: https://www.acmicpc.net/problem/2448
# Difficulty: Gold 4
# Category: 재귀


# Solution 1: recursion
# Time: 1832 ms
# Memory: 214980 KB
class Solution:
    def get_answer(self, n: int):
        size, k = 3, 1
        while n != size:
            size *= 2
            k += 1

        def generate_star(k):
            if k == 1:
                return [[False, False, True, False, False], [False, True, False, True, False], [True, True, True, True, True]]

            prev = generate_star(k - 1)
            padding = [False for _ in range((2 ** k) * 3 // 4)]

            return [
                *list(map(lambda line: [*padding, *line, *padding], prev)),
                *list(map(lambda line: [*line, False, *line], prev))
            ]

        return generate_star(k)


n = int(input())
answer = Solution().get_answer(n)
for line in answer:
    print(''.join(map(lambda c: '*' if c else ' ', line)))
