# 23841. 데칼코마니
# Link: https://www.acmicpc.net/problem/23841
# Difficulty: Bronze 1
# Category: 구현
# Category: 문자열


# Solution 1: implementation, string
# Time: 48 ms
# Memory: 31256 KB
n, m = map(int, input().split())

data = [list(input()) for _ in range(n)]

for row in data:
    result = []
    for i in range(m):
        if row[m - i - 1] != '.':
            result.append(row[m - i - 1])
        else:
            result.append(row[i])
    print(''.join(result))
