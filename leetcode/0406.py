# 406. Queue Reconstruction by Height
# Link: https://leetcode.com/problems/queue-reconstruction-by-height/
# Difficulty: Medium
# Category: Array
# Category: Greedy
# Category: Binary Indexed Tree
# Category: Segment Tree
# Category: Sorting
from typing import List


# Solution 1: greedy algorithm, sorting
# Time: 109 ms
# Memory: 14.6 MB
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []

        for h, k in people:
            queue.insert(k, [h, k])

        return queue
