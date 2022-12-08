# 328. Odd Even Linked List
# Link: https://leetcode.com/problems/odd-even-linked-list/
# Difficulty: Medium
# Category: Linked List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: loop
# Time: 86 ms (O(n))
# Memory: 16.7 MB (O(1))
class Solution1:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        even_head = head.next
        odd, even = head, even_head

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = even_head

        return head
