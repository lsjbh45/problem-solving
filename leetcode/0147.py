# 147. Insertion Sort List
# Link: https://leetcode.com/problems/insertion-sort-list/
# Difficulty: Medium
# Category: Linked List
# Category: Sorting

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: insertion sort
# Time: 1777 ms
# Memory: 17.2 MB
class Solution1:
    def insertionSortList(self, head: Optional[ListNode]) \
            -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node, head = head.next, ListNode(-5001, ListNode(head.val))
        while node:
            pos = head
            while pos.next and pos.next.val <= node.val:
                pos = pos.next
            pos.next = ListNode(node.val, pos.next)
            node = node.next

        return head.next


# Solution 2: insertion sort + additional condition
# Time: 164 ms
# Memory: 17.2 MB
class Solution2:
    def insertionSortList(self, head: Optional[ListNode]) \
            -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node = head
        head = pos = ListNode(-5001)
        while node:
            while pos.next and pos.next.val <= node.val:
                pos = pos.next
            pos.next = ListNode(node.val, pos.next)
            node = node.next
            if node and node.val < pos.val:
                pos = head

        return head.next
