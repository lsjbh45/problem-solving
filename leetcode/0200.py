# 200. Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium
# Category: Array
# Category: Depth-First Search
# Category: Breadth-First Search
# Category: Union Find
# Category: Matrix
from typing import List


# Solution 1: stack
# Time: 533 ms
# Memory: 16.7 MB
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island = 0
        search = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        traversed = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or traversed[i][j]:
                    continue
                island += 1
                stack = [(i, j)]
                while stack:
                    print(stack)
                    x, y = stack.pop()
                    traversed[x][y] = True
                    for dx, dy in search:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            if grid[nx][ny] == '1' and not traversed[nx][ny]:
                                stack.append((nx, ny))

        return island


# Solution 2: recursion
# Time: 267 ms
# Memory: 16.4 MB
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        search = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cnt = 0

        def dfs(i, j):
            grid[i][j] = '0'
            for di, dj in search:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                    dfs(ni, nj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1

        return cnt
