# 687. Longest Univalue Path
# Link: https://leetcode.com/problems/longest-univalue-path/
# Difficulty: Medium
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
# Time: 372 ms
# Memory: 17.9 MB
class Solution1:
    longest = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            height, path = 0, 0
            if node.left and node.left.val == node.val:
                height = max(height, left + 1)
                path += left + 1
            if node.right and node.right.val == node.val:
                height = max(height, right + 1)
                path += right + 1

            self.longest = max(self.longest, path)

            return height

        dfs(root)
        return self.longest
