# 148. Sort List
# Link: https://leetcode.com/problems/sort-list/
# Difficulty: Medium
# Category: Linked List
# Category: Two Pointers
# Category: Divide and Conquer
# Category: Sorting
# Category: Merge Sort
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(node: Optional[ListNode]):
    node_list = []
    while node:
        node_list.append(node.val)
        node = node.next
    return node_list


def to_linked_list(node_list: List[int]) -> Optional[ListNode]:
    head = None
    while node_list:
        head = ListNode(node_list.pop(), head)
    return head


# Solution 1: Heapsort
# Time: 1456 ms
# Memory: 45 MB
class Solution1:
    def heapsort(self, data: List[int]) -> List[int]:
        def heapify(data, index, size):
            largest = index
            left, right = 2 * index + 1, 2 * index + 2
            if left < size and data[left] > data[largest]:
                largest = left
            if right < size and data[right] > data[largest]:
                largest = right
            if largest != index:
                data[largest], data[index] = data[index], data[largest]
                heapify(data, largest, size)

        for i in range(len(data) // 2 - 1, -1, -1):
            heapify(data, i, len(data))

        for i in range(len(data) - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            heapify(data, 0, i)

        return data

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return to_linked_list(self.heapsort(to_list(head)))


# Solution 2: Merge sort
# Time: 845 ms
# Memory: 85.9 MB
class Solution2:
    def mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) \
            -> Optional[ListNode]:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        half, slow, fast = None, head, head
        while slow and fast and fast.next:
            half, slow = slow, slow.next
            fast = fast.next.next
        if half:
            half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeLists(l1, l2)


# Solution 3: Timsort
# Time: 440 ms
# Memory: 45.5 MB
class Solution3:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return to_linked_list(sorted(to_list(head)))
