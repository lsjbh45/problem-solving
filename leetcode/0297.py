# 297. Serialize and Deserialize Binary Tree
# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Difficulty: Hard
# Category: String
# Category: Tree
# Category: Depth-First Search
# Category: Breadth-First Search
# Category: Design
# Category: Binary Tree
import re
from typing import Optional
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


# Solution 1: bfs
# Time: 99 ms
# Memory: 20.1 MB
class Codec:
    def serialize(self, root):
        if not root:
            return '[]'

        data = []
        nodes = deque([root])

        while nodes:
            node = nodes.popleft()

            if node:
                data.append(str(node.val))
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                data.append('null')

        while data[-1] == 'null':
            data.pop()

        return f'[{",".join(data)}]'

    def deserialize(self, data):
        if data == '[]':
            return None

        values = deque(re.sub(r'[\[\]]', '', data).split(','))

        root = TreeNode(values.popleft())
        nodes = deque([root])

        while values:
            node: TreeNode = nodes.popleft()

            left = values.popleft()
            if left != 'null':
                node.left = TreeNode(int(left))
                nodes.append(node.left)

            right = values.popleft() if values else 'null'
            if right != 'null':
                node.right = TreeNode(int(right))
                nodes.append(node.right)

        return root
