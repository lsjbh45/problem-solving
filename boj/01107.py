# 1107. 리모컨
# Link: https://www.acmicpc.net/problem/1107
# Difficulty: Gold 5
# Category: 브루트포스 알고리즘


# Solution 1: brute-force
# Time: 1616 ms
# Memory: 31256 KB
n = int(input())
m = int(input())

break_list = list(map(int, input().split())) if m else []
break_dict = {str(i): (i in break_list) for i in range(10)}

min_cnt = abs(n - 100)
for i in range(1000000):
    if all(not break_dict[c] for c in list(str(i))):
        cnt = abs(n - i) + len(str(i))
        min_cnt = min(min_cnt, cnt)

print(min_cnt)
