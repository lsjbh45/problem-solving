# 5639. 이진 검색 트리
# Link: https://www.acmicpc.net/problem/5639
# Difficulty: Gold 5
# Category: 그래프 이론
# Category: 그래프 탐색
# Category: 트리
# Category: 재귀
from typing import List
import sys
sys.setrecursionlimit(10 ** 6)


# Solution 1: binary search tree
# Time: 3088 ms
# Memory: 52164 KB
class Solution:
    def get_answer(self, nodes: List[int]) -> List[int]:
        class Node:
            def __init__(self, s: int, e: int):
                self.value = nodes[s]
                m = s + 1
                while m <= e:
                    if nodes[m] > self.value:
                        break
                    m += 1
                self.left = type(self)(s + 1, m - 1) if s <= m - 2 else None
                self.right = type(self)(m, e) if m <= e else None

            def post(self) -> List[int]:
                return [*(self.left.post() if self.left else []), *(self.right.post() if self.right else []), self.value]

        tree = Node(0, len(nodes) - 1)
        return tree.post()


nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:  # EOF error
        break
answer = Solution().get_answer(nodes)
for node in answer:
    print(node)
