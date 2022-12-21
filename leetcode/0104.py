# 104. Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy
# Category: Tree
# Category: Depth-First Search
# Category: Breadth-First Search
# Category: Binary Tree
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: DFS
# Time: 100 ms
# Memory: 16.2 MB
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# Solution 2: BFS
# Time: 93 ms
# Memory: 15.3 MB
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        depth = 0

        while q:
            depth += 1

            for _ in range(len(q)):
                sub_root = q.popleft()
                if sub_root.left:
                    q.append(sub_root.left)
                if sub_root.right:
                    q.append(sub_root.right)

        return depth
