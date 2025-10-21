from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        left = 0
        total_cost = 0
        max_freq = 1

        for right in range(1, len(nums)):
            # Cost to make nums[left:right] all equal to nums[right]
            total_cost += (nums[right] - nums[right - 1]) * (right - left)

            # If cost exceeds allowed operations, shrink window from left
            while total_cost > k * numOperations:
                total_cost -= nums[right] - nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq