# 215. Kth Largest Element in an Array
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty: Medium
# Category: Array
# Category: Divide and Conquer
# Category: Sorting
# Category: Heap (Priority Queue)
# Category: Quickselect
from typing import List
import heapq


class MaxBinaryHeap:
    def __init__(self):
        self.items: List[int] = [0]

    def __len__(self):
        return len(self.items) - 1

    def _up_heap(self):
        node, parent = len(self), len(self) // 2
        while parent > 0:
            if self.items[node] <= self.items[parent]:
                break
            self.items[node], self.items[parent] = \
                self.items[parent], self.items[node]
            node, parent = parent, parent // 2

    def insert(self, num):
        self.items.append(num)
        self._up_heap()

    def _down_heap(self, node):
        left, right = node * 2, node * 2 + 1
        max_idx = node
        if left <= len(self) and self.items[left] > self.items[max_idx]:
            max_idx = left
        if right <= len(self) and self.items[right] > self.items[max_idx]:
            max_idx = right
        if max_idx != node:
            self.items[node], self.items[max_idx] = \
                self.items[max_idx], self.items[node]
            self._down_heap(max_idx)

    def extract(self):
        num = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._down_heap(1)
        return num


# Solution 1: heap
# Time: 2709 ms
# Memory: 27.2 MB
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MaxBinaryHeap()
        for num in nums:
            heap.insert(num)
        for _ in range(k - 1):
            heap.extract()
        return heap.extract()


# Solution 2: heapq module
# Time: 668 ms
# Memory: 31 MB
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


# Solution 3: Timsort
# Time: 514 ms
# Memory: 27 MB
class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]
