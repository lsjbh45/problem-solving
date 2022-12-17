# 207. Course Schedule
# Link: https://leetcode.com/problems/course-schedule/
# Difficulty: Medium
# Category: Depth-First Search
# Category: Breadth-First Search
# Category: Graph
# Category: Topological Sort
from typing import List, Dict


# Solution 1: dfs
# Time: 176 ms
# Memory: 16.8 MB
class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: Dict[int, List[int]] = {-1: list(range(numCourses))}
        for course, pre in prerequisites:
            if course not in graph:
                graph[course] = []
            graph[course].append(pre)

        checked = []

        def check(course):
            while course in graph and graph[course]:
                pre = graph[course].pop()
                if pre in checked:
                    return False

                checked.append(pre)
                if not check(pre):
                    return False
                checked.pop()

            return True

        return check(-1)


# Solution 2: dfs, pruning
# Time: 197 ms
# Memory: 16.8 MB
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: Dict[int, List[int]] = {-1: list(range(numCourses))}
        for course, pre in prerequisites:
            if course not in graph:
                graph[course] = []
            graph[course].append(pre)

        visited = []
        checked = []

        def check(course):
            while course in graph and graph[course]:
                pre = graph[course].pop()
                if pre in checked:
                    return False

                if pre in visited:
                    continue

                checked.append(pre)
                if not check(pre):
                    return False
                checked.pop()

                visited.append(pre)

            return True

        return check(-1)
