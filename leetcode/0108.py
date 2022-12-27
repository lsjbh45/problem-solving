# 108. Convert Sorted Array to Binary Search Tree
# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Difficulty: Easy
# Category: Array
# Category: Divide and Conquer
# Category: Tree
# Category: Binary Search Tree
# Category: Binary Tree
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: divide and conquer, recursion
# Time: 58 ms
# Memory: 15.6 MB (O(n log n))
class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        idx = len(nums) // 2
        return TreeNode(
            nums[idx],
            self.sortedArrayToBST(nums[:idx]),
            self.sortedArrayToBST(nums[idx+1:])
        )


# Solution 2: less space
# Time: 54 ms
# Memory: 15.5 MB (O(n))
class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def getBST(s: int, e: int):
            if s > e:
                return None

            m = s + (e - s) // 2
            return TreeNode(nums[m], getBST(s, m - 1), getBST(m + 1, e))

        return getBST(0, len(nums) - 1)
