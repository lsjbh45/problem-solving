# 226. Invert Binary Tree
# Link: https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy
# Category: Tree
# Category: Depth-First Search
# Category: Breadth-First Search
# Category: Binary Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: dfs
# Time: 31 ms
# Memory: 13.9 MB
class Solution1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node:
                node.left, node.right = node.right, node.left
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return root


# Solution 2: dfs post-order
# Time: 30 ms
# Memory: 13.8 MB
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
        return root
