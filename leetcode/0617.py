# 617. Merge Two Binary Trees
# Link: https://leetcode.com/problems/merge-two-binary-trees/
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
# Time: 88 ms
# Memory: 15.5 MB
class Solution1:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 and root2:
            return TreeNode(
                root1.val + root2.val,
                self.mergeTrees(root1.left, root2.left),
                self.mergeTrees(root1.right, root2.right)
            )
        return root1 or root2
