# 9935. 문자열 폭발
# Link: https://www.acmicpc.net/problem/9935
# Difficulty: Gold 4
# Category: 자료 구조
# Category: 문자열
# Category: 스택


# Solution 1: stack
# Time: 220 ms
# Memory: 38064 KB
class Solution:
    def get_answer(self, target: str, exp: str) -> str:
        len_exp = len(exp)

        res = ''
        stack = []

        for c in target + ' ':
            if c == exp[0]:
                if 1 < len_exp:
                    stack.append(1)
                continue
            if stack:
                last_idx = stack.pop()
                if c == exp[last_idx]:
                    if last_idx + 1 < len_exp:
                        stack.append(last_idx + 1)
                    continue
                stack.append(last_idx)
            for idx in stack:
                res += exp[:idx]
            stack = []
            res += c

        return res[:-1] if len(res) > 1 else 'FRULA'


target = input()
exp = input()
answer = Solution().get_answer(target, exp)
print(answer)
