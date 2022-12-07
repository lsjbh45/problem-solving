# 234. Palindrome Linked List
# Link: https://leetcode.com/problems/palindrome-linked-list/
# Difficulty: Easy
# Category: Linked List
# Category: Two Pointers
# Category: Stack
# Category: Recursion
from typing import Optional, Deque
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def data(self):
        return self.val, self.next.data() if self.next else None


# Solution 1: deque
# Time: 808 ms
# Memory: 47.4 MB
class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes: Deque[int] = deque()
        node: Optional[ListNode] = head

        while node:
            nodes.append(node.val)
            node = node.next

        while len(nodes) > 1:
            if nodes.popleft() != nodes.pop():
                return False

        return True


# Solution 2: runner
# Time: 1899 ms
# Memory: 31.3 MB
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev: Optional[ListNode] = None
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while slow and slow.val == rev.val:
            slow, rev = slow.next, rev.next

        return not slow
