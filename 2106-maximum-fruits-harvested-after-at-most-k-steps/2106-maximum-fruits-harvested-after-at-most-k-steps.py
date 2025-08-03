from typing import List
import bisect

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        positions = [pos for pos, _ in fruits]
        prefix_sum = [0] * (n + 1)

        # Build prefix sum of fruit amounts
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + fruits[i][1]

        def get_sum(left: int, right: int) -> int:
            """Return total fruits between indices left and right (inclusive)."""
            return prefix_sum[right + 1] - prefix_sum[left]

        max_fruits = 0

        # Try all possible left-first strategies
        for i in range(n):
            left_pos = fruits[i][0]
            steps_left = abs(startPos - left_pos)
            if steps_left > k:
                continue
            remaining_steps = k - steps_left
            max_right_pos = max(startPos, left_pos + remaining_steps)
            j = bisect.bisect_right(positions, max_right_pos) - 1
            max_fruits = max(max_fruits, get_sum(i, j))

        # Try all possible right-first strategies
        for j in range(n):
            right_pos = fruits[j][0]
            steps_right = abs(right_pos - startPos)
            if steps_right > k:
                continue
            remaining_steps = k - steps_right
            min_left_pos = min(startPos, right_pos - remaining_steps)
            i = bisect.bisect_left(positions, min_left_pos)
            max_fruits = max(max_fruits, get_sum(i, j))

        return max_fruits
