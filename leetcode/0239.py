# 239. Sliding Window Maximum
# Link: https://leetcode.com/problems/sliding-window-maximum/
# Difficulty: Hard
# Category: Array
# Category: Queue
# Category: Sliding Window
# Category: Heap (Priority Queue)
# Category: Monotonic Queue
from typing import List
import heapq
from collections import deque


# Solution 1:
# Time: Time Limit Exceeded
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def findMax(s, e):
            mv, mi = -10001, -1
            for i in range(s, e + 1):
                if nums[i] > mv:
                    mv, mi = nums[i], i
            return mv, mi

        mw = []
        mv, mi = findMax(0, k - 1)
        for i in range(k - 1, len(nums)):
            if mi < i - k + 1:
                mv, mi = findMax(i - k + 1, i)
            if nums[i] > mv:
                mv, mi = nums[i], i
            mw.append(mv)

        return mw


# Solution 2: priority queue
# Time: 1992 ms
# Memory: 34.5 MB
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        for i in range(k - 1):
            heapq.heappush(pq, (-nums[i], i, nums[i]))

        idx, num = -1, -10001
        mw = []
        for i in range(k - 1, len(nums)):
            heapq.heappush(pq, (-nums[i], i, nums[i]))
            while idx < i - k + 1 or num < nums[i]:
                _, idx, num = heapq.heappop(pq)
            mw.append(num)

        return mw


# Solution 3: deque
# Time: 1662 ms
# Memory: 30 MB
class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        result = []

        for i in range(len(nums)):
            if q and i - q[0] == k:
                q.popleft()

            while q:
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break

            q.append(i)

            if i >= k - 1:
                result.append(nums[q[0]])

        return result
