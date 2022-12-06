# 42. Trapping Rain Water
# Link: https://leetcode.com/problems/trapping-rain-water/
# Difficulty: Hard
# Category: Array
# Category: Two Pointers
# Category: Dynamic Programming
# Category: Stack
# Category: Monotonic Stack

from typing import List


# Solution 1. brute-force
# Time: 1245 ms (O(n^2))
# Memory: 17.3 MB
class Solution1:
    def trap(self, height: List[int]) -> int:
        water = [0 for _ in range(len(height))]
        height_idx = [(i, x) for i, x in enumerate(height)]
        height_idx.sort(key=lambda x: x[1])

        i1, h1 = 0, 0
        for i2, h2 in height_idx:
            start, end = min(i1, i2), max(i1, i2)
            water[start + 1:end] = [h1 for _ in range(end - start - 1)]
            i1, h1 = i2, h2

        total = 0
        for i in range(len(height)):
            if water[i] > height[i]:
                total += water[i] - height[i]

        return total


# Solution 2. two pointer
# Time: 129 ms (O(n))
# Memory: 16.1 MB
class Solution2:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        volume = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                volume += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                volume += right_max - height[right]

        return volume


# Solution 3. stack
# Time: 128 ms (O(n))
# Memory: 15.9 MB
class Solution3:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for right in range(len(height)):
            # 높이가 이전보다 높아지면, 해당 높이보다 낮은 처리되지 않은 부분을 처리
            while stack and height[right] > height[stack[-1]]:
                target = stack.pop()

                if not stack:
                    break
                left = stack[-1]

                distance = right - left - 1
                water = min(height[left], height[right]) - height[target]
                volume += distance * water
            stack.append(right)
        return volume
