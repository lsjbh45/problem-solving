# 1991. 트리 순회
# Link: https://www.acmicpc.net/problem/1991
# Difficulty: Silver 1
# Category: 트리
# Category: 재귀
from typing import Dict, Tuple


# Solution 1: dfs
# Time: 136 ms
# Memory: 37760 KB
class Traverse:
    def __init__(self, tree: Dict[str, Tuple[str, str]]):
        self.tree = tree

    def preorder(self, node: str):
        if node == '.':
            return []
        left, right = self.tree[node]
        return [node, *self.preorder(left), *self.preorder(right)]

    def inorder(self, node: str):
        if node == '.':
            return []
        left, right = self.tree[node]
        return [*self.inorder(left), node, *self.inorder(right)]

    def postorder(self, node: str):
        if node == '.':
            return []
        left, right = self.tree[node]
        return [*self.postorder(left), *self.postorder(right), node]


n = int(input())
tree = {n: (l, r) for n, l, r in [input().split() for _ in range(n)]}
traverse = Traverse(tree)
print(''.join(traverse.preorder('A')))
print(''.join(traverse.inorder('A')))
print(''.join(traverse.postorder('A')))
