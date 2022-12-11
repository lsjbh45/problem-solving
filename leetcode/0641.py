# 641. Design Circular Deque
# Link: https://leetcode.com/problems/design-circular-deque/
# Difficulty: Medium
# Category: Array
# Category: Linked List
# Category: Design
# Category: Queue
from typing import Optional


# Solution1: array
# Time: 75 ms
# Memory: 14.6 MB
class MyCircularDeque1:
    def __init__(self, k: int):
        self.size = k
        self.data = [-1] * (k + 1)
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % (self.size + 1)
        self.data[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % (self.size + 1)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % (self.size + 1)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % (self.size + 1)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.rear - 1) % (self.size + 1)]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.front - self.rear) % (self.size + 1) == 1


# Solution 2: doublely linked list
# Time: 188 ms
# Memory: 15 MB
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next


class MyCircularDeque2:
    def __init__(self, k: int):
        self.front: Optional[ListNode] = None
        self.rear: Optional[ListNode] = None
        self.size = 0
        self.max = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = ListNode(value, None, self.front)
        if self.front.next:
            self.front.next.prev = self.front
        else:
            self.rear = self.front

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = ListNode(value, self.rear, None)
        if self.rear.prev:
            self.rear.prev.next = self.rear
        else:
            self.front = self.rear

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if not self.front:
            return False

        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.rear:
            return False

        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None

        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.front.val if self.front else -1

    def getRear(self) -> int:
        return self.rear.val if self.rear else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max
