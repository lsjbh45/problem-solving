# 24. Swap Nodes in Pairs
# Link: https://leetcode.com/problems/swap-nodes-in-pairs/
# Difficulty: Medium
# Category: Linked List
# Category: Recursion
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution1: recursion
# Time: 39 ms
# Memory: 14 MB
class Solution1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(head.next.next)
            p.next = head
            return p
        return head


# Solution2: loop
# Time: 39 ms
# Memory: 13.9 MB
class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = node = ListNode(-1, head)

        while head and head.next:
            node.next = head.next
            head.next = head.next.next
            node.next.next = head

            node = head
            head = head.next

        return root.next
