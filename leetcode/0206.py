# 206. Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
# Category: Linked List
# Category: Recursion
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: loop
# Time: 87 ms
# Memory: 15.5 MB
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev: Optional[ListNode] = None

        while head:
            rev, rev.next, head = head, rev, head.next

        return rev


# Solution 2: recursion
# Time: 77 ms
# Memory: 20.5 MB
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseRec(target: Optional[ListNode], rev: Optional[ListNode]):
            if not target:
                return rev
            target, rev, rev.next = target.next, target, rev
            return reverseRec(target, rev)

        return reverseRec(head, None)
