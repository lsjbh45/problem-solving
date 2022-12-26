# 617. Merge Two Binary Trees
# Link: https://leetcode.com/problems/merge-two-binary-trees/
# Difficulty: Easy
# Category: Tree
# Category: Depth-First Search
# Category: Binary Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: dfs
# Time: 54 ms
# Memory: 18.8 MB
class Solution1:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int | None:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left is None or right is None:
                return None

            if abs(left - right) > 1:
                return None

            print(node.val, left, right)
            return max(left, right) + 1

        return dfs(root) is not None
