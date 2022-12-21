# 543. Diameter of Binary Tree
# Link: https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy
# Category: Tree
# Category: Depth-First Search
# Category: Binary Tree
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: dfs
# Time: 91 ms
# Memory: 16.4 MB
class Solution1:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getLengthAndDiameter(root: TreeNode) -> Tuple[int, int]:
            l_len, l_dia = getLengthAndDiameter(
                root.left) if root.left else (0, 0)
            r_len, r_dia = getLengthAndDiameter(
                root.right) if root.right else (0, 0)

            c_len = max(l_len, r_len) + 1
            c_dia = max(l_dia, r_dia, l_len + r_len)

            return (c_len, c_dia)

        _, dia = getLengthAndDiameter(root) if root else (0, 0)
        return dia


# Solution 2: dfs with accumulation
# Time: 102 ms
# Memory: 16.3 MB
class Solution2:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            self.diameter = max(self.diameter, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.diameter
