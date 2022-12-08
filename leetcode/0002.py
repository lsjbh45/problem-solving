# 2. Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium
# Category: Linked List
# Category: Math
# Category: Recursion
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: loop
# Time: 73 ms
# Memory: 14 MB
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = head = ListNode(-1)

        while l1 or l2 or carry:
            print(l1, l2, carry)
            l1 = l1 if l1 else ListNode(0)
            l2 = l2 if l2 else ListNode(0)

            carry, add = divmod(l1.val + l2.val + carry, 10)

            head.next = ListNode(add)
            head = head.next

            l1, l2 = l1.next, l2.next

        return result.next


# Solution 2: recursion
# Time: 99 ms
# Memory: 14.1 MB
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        def addRec(l1: Optional[ListNode], l2: Optional[ListNode],
                   carry: int = 0) -> Optional[ListNode]:
            if not l1 and not l2 and not carry:
                return None

            l1 = l1 if l1 else ListNode(0)
            l2 = l2 if l2 else ListNode(0)

            add = l1.val + l2.val + carry
            add, carry = add % 10, add // 10

            return ListNode(add, addRec(l1.next, l2.next, carry))

        return addRec(l1, l2, 0)


# Solution 3: type conversion
# Time: 107 ms
# Memory: 13.9 MB
class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev: Optional[ListNode] = None

        while head:
            rev, rev.next, head = head, rev, head.next

        return rev

    def toPythonList(self, head: Optional[ListNode]) -> List[int]:
        lst: List = []

        while head:
            lst.append(head.val)
            head = head.next

        return lst

    def toReversedList(self, lst: List[int]) -> Optional[ListNode]:
        node: ListNode = ListNode(0)
        head: ListNode = node

        while lst:
            head.next = ListNode(lst.pop())
            head = head.next

        return node.next

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        pl1 = self.toPythonList(self.reverseList(l1))
        pl2 = self.toPythonList(self.reverseList(l2))

        return self.toReversedList([int(c) for c in str(
            int(''.join(map(str, pl1))) + int(''.join(map(str, pl2)))
        )])
