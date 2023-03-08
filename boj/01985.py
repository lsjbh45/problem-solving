# 1985. 디지털 친구
# Link: https://www.acmicpc.net/problem/1985
# Difficulty: Silver 4
# Category: 문자열
# Category: 브루트포스 알고리즘

# Solution 1: string, set
# Time: 44 ms
# Memory: 31256 KB
def check_friend(x, y):
    return set(x) == set(y)


def check_almost_friend(x, y):
    for i in range(len(y) - 1):
        a, b = str(int(y[i]) + 1), str(int(y[i + 1]) - 1)
        if len(a) == 1 and len(b) == 1:
            if check_friend(x, y[:i] + y[i+2:] + a + b):
                return True
        a, b = str(int(y[i]) - 1), str(int(y[i + 1]) + 1)
        if len(a) == 1 and len(b) == 1:
            if check_friend(x, y[:i] + y[i+2:] + a + b):
                if i > 0 or a != '0':
                    return True
    return False


for _ in range(3):
    x, y = input().split()
    if check_friend(x, y):
        print('friends')
    elif check_almost_friend(x, y) or check_almost_friend(y, x):
        print('almost friends')
    else:
        print('nothing')
