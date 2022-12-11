# 23. Merge k Sorted Lists
# Link: https://leetcode.com/problems/merge-k-sorted-lists/
# Difficulty: Hard
# Category: Linked List
# Category: Divide and Conquer
# Category: Heap (Priority Queue)
# Category: Merge Sort
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def data(self):
        return self.val, self.next.data() if self.next else None


# Solution 1:
# Time: 6541 ms
# Memory: 17.5 MB
class Solution1:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        merged = head = ListNode(-1)

        while True:
            idx, val = -1, 10 ** 4 + 1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if lists[i].val < val:
                    idx, val = i, lists[i].val
            if idx == -1:
                break

            head.next = ListNode(val)
            head = head.next

            lists[idx] = lists[idx].next

        return merged.next


# Solution 2: priority queue
# Time: 226 ms
# Memory: 18.1 MB
class Solution2:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        heap = [(lst.val, idx, lst) for idx, lst in enumerate(lists) if lst]
        heapq.heapify(heap)

        root = head = ListNode(-1)
        while heap:
            _, idx, head.next = heapq.heappop(heap)
            head = head.next
            if head.next:
                heapq.heappush(heap, (head.next.val, idx, head.next))

        return root.next
