# 13140. Hello World!
# Link: https://www.acmicpc.net/problem/13140
# Difficulty: Bronze 4
# Category: 수학
# Category: 브루트포스 알고리즘


# Soltion 1: brute-force
# Time: 344 ms
# Memory: 31256 KB
def find_case(N):
    for l in range(10):
        rs = {n for n in range(10) if n != l}
        for r in rs:
            ds = {n for n in rs if n != r}
            for d in ds:
                es = {n for n in ds if n != d}
                for e in es:
                    os = {n for n in es if n != e}
                    for o in os:
                        hs = {n for n in os if n != o and n != 0}
                        for h in hs:
                            ws = {n for n in hs if n != h and n != 0}
                            for w in ws:
                                case = check_case(N, d, e, h, l, o, r, w)
                                if case:
                                    return case


def check_case(N, d, e, h, l, o, r, w):
    a = (((h * 10 + e) * 10 + l) * 10 + l) * 10 + o
    b = (((w * 10 + o) * 10 + r) * 10 + l) * 10 + d
    if a + b == N:
        return (a, b)


N = int(input())
result = find_case(N)
if not result:
    print('No Answer')
else:
    a, b = result
    print(f'  {a}')
    print(f'+ {b}')
    print('-------')
    print(format(N, '7d'))
'''
98001
76502
174503
'''
