# 622. Design Circular Queue
# Link: https://leetcode.com/problems/design-circular-queue/
# Difficulty: Medium
# Category: Array
# Category: Linked List
# Category: Design
# Category: Queue


# Solution 1: use (k+1) spaces
# Time: 193 ms
# Memory: 14.6 MB
class MyCircularQueue1:
    def __init__(self, k: int):
        self.size = k
        self.front = 0
        self.rear = k
        self.data = [-1] * (k + 1)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % (self.size + 1)
        self.data[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % (self.size + 1)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.rear]

    def isEmpty(self) -> bool:
        return (self.rear - self.front) % (self.size + 1) == self.size

    def isFull(self) -> bool:
        return (self.rear - self.front) % (self.size + 1) == self.size - 1


# Solution 2: use k spaces
# Time: 181 ms
# Memory: 14.6 MB
class MyCircularQueue2:
    def __init__(self, k: int):
        self.size = k
        self.front = 0
        self.rear = 0
        self.data = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.front] = -1
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.data[self.front] == -1

    def isFull(self) -> bool:
        return self.front == self.rear and self.data[self.front] != -1
