# 938. Range Sum of BST
# Link: https://leetcode.com/problems/range-sum-of-bst/
# Difficulty: Easy
# Category: Tree
# Category: Depth-First Search
# Category: Binary Search Tree
# Category: Binary Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: dfs, pruning
# time: 215 ms
# Memory: 23.2 MB
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) \
            -> int:
        if not root:
            return 0

        rsum: int = 0
        if root.val > low:
            rsum += self.rangeSumBST(root.left, low, high)
        if low <= root.val <= high:
            rsum += root.val
        if root.val < high:
            rsum += self.rangeSumBST(root.right, low, high)
        return rsum
