# 1038. Binary Search Tree to Greater Sum Tree
# Link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Difficulty: Medium
# Category: Tree
# Category: Depth-First Search
# Category: Binary Search Tree
# Category: Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: dfs, in-order
# Time: 27 ms
# Memory: 13.9 MB
class Solution1:
    acc = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right:
            self.bstToGst(root.right)

        self.acc += root.val
        root.val = self.acc

        if root.left:
            self.bstToGst(root.left)

        return root
