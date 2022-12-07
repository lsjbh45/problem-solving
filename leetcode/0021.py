# 21. Merge Two Sorted Lists
# Link: https://leetcode.com/problems/palindrome-linked-list/
# Difficulty: Easy
# Category: Linked List
# Category: Recursion
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1:
# Time: 36 ms
# Memory: 14 ms
class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:

        head = tail = None
        while list1 or list2:
            if not list1:
                node, list2 = list2, None
            elif not list2:
                node, list1 = list1, None
            else:
                if list1.val <= list2.val:
                    node, list1 = ListNode(list1.val), list1.next
                else:
                    node, list2 = ListNode(list2.val), list2.next
            if not tail:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next

        return head


# Solution 2: recursion
# Time: 83 ms
# Memory: 14 ms
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
