# 783. Minimum Distance Between BST Nodes
# Link: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Difficulty: Easy
# Category: Tree
# Category: Depth-First Search
# Category: Breadth-First Search
# Category: Binary Search Tree
# Category: Binary Tree
import sys
from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1:
# Time: 27 ms
# Memory: 13.9 MB
class Solution1:
    minDiff = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        def getMost(node: TreeNode) -> Tuple[int, int]:
            l_lm, l_rm = getMost(node.left) \
                if node.left else (node.val, -sys.maxsize)
            r_lm, r_rm = getMost(node.right) \
                if node.right else (sys.maxsize, node.val)

            self.minDiff = min(self.minDiff, node.val - l_rm, r_lm - node.val)

            return (l_lm, r_rm)

        getMost(root)
        return self.minDiff


# Solution 2: dfs, in-order
# Time: 37 ms
# Memory: 13.9 MB
class Solution2:
    prev = -sys.maxsize
    minDiff = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.minDiff = min(self.minDiff, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.minDiff
