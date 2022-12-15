# 706. Design HashMap
# Link: https://leetcode.com/problems/design-hashmap/
# Difficulty: Easy
# Category: Array
# Category: Hash Table
# Category: Linked List
# Category: Design
# Category: Hash Function
from collections import defaultdict


class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


# Solution 1: separate chaining
# Time: 254 ms
# Memory: 17.5 MB
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.data = defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        head = self.data[idx]

        while head.next:
            if head.next.key == key:
                head.next.value = value
                return
            head = head.next

        head.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        head = self.data[idx].next

        while head:
            if head.key == key:
                return head.value
            head = head.next

        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        head = self.data[idx]

        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next
