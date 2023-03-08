# 17202. 핸드폰 번호 궁합
# Link: https://www.acmicpc.net/problem/17202
# Difficulty: Bronze 1
# Category: 구현
# Category: 다이나믹 프로그래밍
# Category: 문자열


# Soltion 1: implementation
# Time: 44 ms
# Memory: 31256 KB
a = map(int, list(input()))
b = map(int, list(input()))
lst = sum(map(list, zip(a, b)), [])

while len(lst) > 2:
    lst = [(lst[i] + lst[i + 1]) % 10 for i in range(len(lst) - 1)]

print(''.join(map(str, lst)))
