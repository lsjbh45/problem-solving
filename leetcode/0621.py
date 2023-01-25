# 621. Task Scheduler
# Link: https://leetcode.com/problems/task-scheduler/
# Difficulty: Medium
# Category: Array
# Category: Hash Table
# Category: Greedy
# Category: Sorting
# Category: Heap (Priority Queue)
# Category: Counting
from collections import Counter
from typing import List


# Solution 1: greedy algorithm
# Time: 3380 ms
# Memory: 14.5 MB
class Solution1:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = {}
        for task in tasks:
            if task not in cnt:
                cnt[task] = 0
            cnt[task] += 1

        cd = {t: 1 for t in tasks}
        time = 0

        while cnt:
            time += 1
            for t, _ in sorted(cnt.items(), key=lambda x: -x[1]):
                if cd[t] <= time:
                    cd[t] = time + n + 1
                    cnt[t] -= 1
                    if not cnt[t]:
                        cnt.pop(t)
                    break

        return time


# Solution 2: greedy algorithm, counter
# Time: 712 ms
# Memory: 14.2 MB
class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        result = 0

        while cnt:
            task = 0
            for t, _ in cnt.most_common(n + 1):
                cnt.subtract(t)
                task += 1

            cnt += Counter()  # remove from cnt if count is lte 0
            result += n + 1 if cnt else task

        return result
