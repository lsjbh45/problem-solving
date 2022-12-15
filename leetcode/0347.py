# 3. Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Category: Array
# Category: Hash Table
# Category: Divide and Conquer
# Category: Sorting
# Category: Heap (Priority Queue)
# Category: Bucket Sort
# Category: Counting
# Category: Quickselect
from typing import List
from collections import Counter
import heapq


# Solution 1: most_common
# Time: 113 ms
# Memory: 18.5 MB
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [elem for elem, _ in Counter(nums).most_common(k)]


# Solution 2: heap
# Time: 108 ms
# Memory: 18.5 MB
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [(-freq, elem) for elem, freq in Counter(nums).most_common(k)]
        heapq.heapify(heap)

        topKFrequent = []
        for _ in range(k):
            _, elem = heapq.heappop(heap)
            topKFrequent.append(elem)

        return topKFrequent


# Solution 3: zip, unpacking
# Time: 112 ms
# Memory: 18.5 MB
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(list(zip(*Counter(nums).most_common(k)))[0])
