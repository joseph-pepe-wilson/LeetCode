from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):  # Iterate through possible subarrays
            if nums[i] + nums[i + 2] == nums[i + 1] / 2:
                count += 1  # Increment count if condition is met
        return count
