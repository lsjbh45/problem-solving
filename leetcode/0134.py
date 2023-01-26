# 134. Gas Station
# Link: https://leetcode.com/problems/gas-station/
# Difficulty: Medium
# Category: Array
# Category: Greedy
from typing import List


# Solution 1:
# Time: 1132 ms
# Memory: 19.3 MB
class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        d = [gas[i] - cost[i] for i in range(len(gas))]

        acc = 0
        min_acc = 10 ** 9
        min_idx = -1
        for i, di in enumerate(d):
            acc += di
            if min_acc > acc:
                min_acc = acc
                min_idx = i
        if acc < 0:
            return -1
        return (min_idx + 1) % len(d)


# Solution 2: greedy algorithm
# Time: 1461 ms
# Memory: 19.7 MB
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        fuel = 0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                start = i + 1
                fuel = 0
        return start
