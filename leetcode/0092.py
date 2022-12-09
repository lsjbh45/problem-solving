# 92. Reverse Linked List II
# Link: https://leetcode.com/problems/reverse-linked-list-ii/
# Difficulty: Medium
# Category: Linked List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def data(self):
        return self.val, self.next.data() if self.next else None


# Solution1: loop
# Time: 37 ms
# Memory: 14.1 MB
class Solution1:
    def reverseBetween(self, head: Optional[ListNode],
                       left: int, right: int) -> Optional[ListNode]:
        root = node = ListNode(0)
        root.next = head
        for _ in range(left - 1):
            node = node.next

        target = end = node.next
        rev = None
        for _ in range(right - left + 1):
            rev, rev.next, target = target, rev, target.next

        node.next = rev
        end.next = target

        return root.next
