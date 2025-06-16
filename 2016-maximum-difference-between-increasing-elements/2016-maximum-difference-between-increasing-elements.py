from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = nums[0]
        max_diff = -1

        for num in nums[1:]:  # Start from index 1
            if num > min_value:
                max_diff = max(max_diff, num - min_value)
            min_value = min(min_value, num)  # Update min value

        return max_diff
