# 240. Search a 2D Matrix II
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
# Difficulty: Medium
# Category: Array
# Category: Binary Search
# Category: Divide and Conquer
# Category: Matrix
from typing import List


# Solution 1: binary search
# Time: 186 ms
# Memory: 21 MB
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def rec(x1, x2, y1, y2):
            if x1 > x2 or y1 > y2:
                return False
            xm = x1 + (x2 - x1) // 2
            ym = y1 + (y2 - y1) // 2
            if target > matrix[xm][ym]:
                return rec(x1, xm, ym + 1, y2) \
                    or rec(xm + 1, x2, y1, ym) \
                    or rec(xm + 1, x2, ym + 1, y2)
            elif target < matrix[xm][ym]:
                return rec(x1, xm - 1, y1, ym - 1) \
                    or rec(xm, x2, y1, ym - 1) \
                    or rec(x1, xm - 1, ym, y2)
            else:
                return True
        return rec(0, len(matrix) - 1, 0, len(matrix[0]) - 1)


# Solution 2: search from corner
# Time: 426 ms
# Memory: 20.4 MB
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = 0, len(matrix[0]) - 1

        while x <= len(matrix) - 1 and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False


# Solution 3: brute-force
# Time: 154 ms
# Memory: 20.3 MB
class Solution3:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)
