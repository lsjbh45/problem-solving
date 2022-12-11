# 232. Implement Queue using Stacks
# Link: https://leetcode.com/problems/implement-queue-using-stacks/
# Difficulty: Easy
# Category: Stack
# Category: Design
# Category: Queue


# Solution 1: reverse at push
# Time: 64 ms (O(n))
# Memory: 14.1 MB
class MyQueue1:
    def __init__(self):
        self.data = []
        self.sub = []

    def push(self, x: int) -> None:
        for _ in range(len(self.data)):
            self.sub.append(self.data.pop())
        self.data.append(x)
        for _ in range(len(self.sub)):
            self.data.append(self.sub.pop())

    def pop(self) -> int:
        return self.data.pop()

    def peek(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return not len(self.data)


# Solution 2: reverse at peek
# Time: 34 ms (O(1))
# Memory: 13.9 MB
class MyQueue2:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            for _ in range(len(self.input)):
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not len(self.input) and not len(self.output)
