from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = float('-inf')
        n = len(nums)

        for i in range(n):
            diff = abs(nums[i] - nums[(i + 1) % n])  # Circular adjacency
            max_diff = max(max_diff, diff)

        return max_diff
