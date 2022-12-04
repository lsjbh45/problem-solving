# 937. Reorder Data in Log Files
# Link: https://leetcode.com/problems/reorder-data-in-log-files/
# Difficulty: Medium
# Category: String
# Category: Array
# Category: Sorting
from typing import List


# Solution 1: lambda expression
# Time: 41 ms
# Memory: 13.9 MB
class Solution1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []

        for log in logs:
            if log.split(' ')[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        letter_logs.sort(key=lambda log: (
            ' '.join(log.split(' ')[1:]), log.split(' ')[0]
        ))

        return letter_logs + digit_logs
