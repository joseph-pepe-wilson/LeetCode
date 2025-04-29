from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)  # Find the maximum element
        count = 0
        left = 0
        freq = 0  # Frequency of max_num in the current window

        for right in range(len(nums)):
            if nums[right] == max_num:
                freq += 1

            # Shrink the window until max_num appears at least k times
            while freq >= k:
                count += len(nums) - right
                if nums[left] == max_num:
                    freq -= 1
                left += 1

        return count
