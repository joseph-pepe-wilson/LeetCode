from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        min_position = -1
        max_position = -1
        boundary = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:  
                boundary = i  # Reset the boundary for valid subarrays
            
            if num == minK:  
                min_position = i  # Update last seen index of minK
            
            if num == maxK:  
                max_position = i  # Update last seen index of maxK
            
            # A valid subarray must contain both minK and maxK
            count += max(0, min(min_position, max_position) - boundary)
        
        return count
