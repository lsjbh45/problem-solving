# 2205. 저울 추 만들기
# Link: https://www.acmicpc.net/problem/2205
# Difficulty: Silver 1
# Category: 수학
# Category: 그리디 알고리즘


# Solution 1:
# Time: 52 ms
# Memory: 31256 KB
def next_square(num):
    next_square = 2 ** 1
    while next_square <= num:
        next_square *= 2
    return next_square


n = int(input())

result = [0 for _ in range(n + 1)]

max_square = next_square(n)
possible = n
next_possible = max_square - n - 1

for i in range(n, 0, -1):
    if max_square - (i + 1) > possible:
        possible = next_possible
        max_square = next_square(i + 1)
        next_possible = max_square - (i + 2)
    result[i] = max_square - (i + 1)
for data in result:
    print(data)


# Solution 2: Greedy
# Time: 52 ms
# Memory: 31256 KB
n = int(input())

max_square = 2 ** 1
while max_square <= n:
    max_square *= 2

used = [i > n for i in range(max_square + 1)]
result = [0 for _ in range(n + 1)]

for i in range(n, 0, -1):
    square = max_square
    while used[square - i]:
        square //= 2
    used[square - i] = True
    result[i] = square - i
for data in result[1:]:
    print(data)
