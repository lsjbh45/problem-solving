# 225. Implement Stack using Queues
# Link: https://leetcode.com/problems/implement-stack-using-queues/
# Difficulty: Easy
# Category: Stack
# Category: Design
# Category: Queue
from collections import deque


# Solution 1: use 2 queues
# Time: 60 ms
# Memory: 13.9 ms
class MyStack1:
    def __init__(self):
        self.data = deque()
        self.sub = deque()

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        if not self.data:
            self.data, self.sub = self.sub, self.data
        while len(self.data) > 1:
            self.sub.append(self.data.popleft())
        return self.data.pop()

    def top(self) -> int:
        if not self.data:
            self.data, self.sub = self.sub, self.data
        while len(self.data) > 1:
            self.sub.append(self.data.popleft())
        return self.data[0]

    def empty(self) -> bool:
        return not self.data and not self.sub


# Solution 2: use 1 queue
# Time: 41 ms
# Memory: 14.1 MB
class MyStack2:
    def __init__(self):
        self.data = deque()

    def push(self, x: int) -> None:
        self.data.append(x)
        for _ in range(len(self.data) - 1):
            self.data.append(self.data.popleft())

    def pop(self) -> int:
        return self.data.popleft()

    def top(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return not len(self.data)


obj = MyStack2()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())
