# 5554. 심부름 가는 길
# Link: https://www.acmicpc.net/problem/5554
# Difficulty: Bronze 4
# Category: 수학
# Category: 구현
# Category: 사칙연산


# Soltion 1: implementation
# Time: 44 ms
# Memory: 31256 KB
time = [int(input()) for _ in range(4)]
total = sum(time)
x, y = total // 60, total % 60
print(f'{x}\n{y}')
