# 4159. 알래스카
# Link: https://www.acmicpc.net/problem/4159
# Difficulty: Silver 3
# Category: 그리디 알고리즘
# Category: 정렬


# Soltion 1: greedy, sorting
# Time: 120 ms
# Memory: 31256 KB
def checkPossible(pos):
    pos.sort()

    for i in range(len(pos) - 1):
        if pos[i + 1] - pos[i] > 200:
            return 'IMPOSSIBLE'

    if 1422 - pos[-1] > 100:
        return 'IMPOSSIBLE'

    return 'POSSIBLE'


n = int(input())
while n:
    pos = [int(input()) for _ in range(n)]

    print(checkPossible(pos))
    n = int(input())
