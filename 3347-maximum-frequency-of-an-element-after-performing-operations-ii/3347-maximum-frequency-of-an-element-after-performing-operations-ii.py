from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        left = 0
        total_cost = 0
        max_freq = 0

        for right in range(len(nums)):
            # Cost to make nums[left:right] all equal to nums[right]
            total_cost += (nums[right] - nums[right - 1]) * (right - left) if right > 0 else 0

            # If cost exceeds the allowed range, shrink the window
            while total_cost > k * numOperations:
                total_cost -= nums[right] - nums[left]
                left += 1

            # Update max frequency
            max_freq = max(max_freq, right - left + 1)

        return max_freq