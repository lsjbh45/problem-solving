# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Difficulty: Medium
# Category: Array
# Category: Hash Table
# Category: Divide and Conquer
# Category: Tree
# Category: Binary Tree
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: divide-and-conquer
# Time: 407 ms
# Memory: 88.5 MB
class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) \
            -> Optional[TreeNode]:
        if not preorder:
            return None

        for i in range(len(inorder)):
            if preorder[0] == inorder[i]:
                return TreeNode(
                    preorder[0],
                    self.buildTree(preorder[1:i+1], inorder[:i]),
                    self.buildTree(preorder[i+1:], inorder[i+1:])
                )


# Solution 2: divide-and-conquer, chracteristic of pre-order
# Time: 69 ms
# Memory: 18.9 MB
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) \
            -> Optional[TreeNode]:
        pre_iter = iter(preorder)
        in_dict = {v: i for i, v in enumerate(inorder)}

        def rec(start, end):
            if start <= end:
                val = next(pre_iter)
                idx = in_dict[val]

                return TreeNode(val, rec(start, idx - 1), rec(idx + 1, end))

        return rec(0, len(preorder) - 1)
