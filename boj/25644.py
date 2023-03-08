# 25644. 최대 상승
# Link: hhttps://www.acmicpc.net/problem/25644
# Difficulty: Silver 5
# Category: 구현
# Category: 다이나믹 프로그래밍
# Category: 그리디 알고리즘


# Solution 1: greedy
# Time: 204 ms
# Memory: 54752 KB
n = int(input())
a_list = list(map(int, input().split()))

max_profit = 0
buy = 10 ** 9 + 1

for a in a_list:
    buy = min(buy, a)
    max_profit = max(max_profit, a - buy)

print(max_profit)
