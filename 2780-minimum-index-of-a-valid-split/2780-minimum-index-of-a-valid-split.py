from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the dominant element in the entire array.
        total_count = Counter(nums)
        dominant = None
        for key, count in total_count.items():
            if count > len(nums) // 2:
                dominant = key
                break
        
        # Step 2: Iterate through the array to determine a valid split.
        left_count = 0
        for i in range(len(nums)):
            # Increment the count for the dominant element in the left subarray.
            if nums[i] == dominant:
                left_count += 1
            
            # Calculate the sizes of the left and right subarrays.
            left_size = i + 1
            right_size = len(nums) - left_size
            
            # Check if the current split is valid.
            if (left_count * 2 > left_size) and ((total_count[dominant] - left_count) * 2 > right_size):
                return i
        
        # If no valid split is found, return -1.
        return -1
