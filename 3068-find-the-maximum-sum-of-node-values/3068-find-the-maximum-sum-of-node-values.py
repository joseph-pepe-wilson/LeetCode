from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total_sum = sum(nums)
        diff_sum = 0
        min_diff = float('inf')
        change_count = 0
        
        for num in nums:
            xor_val = num ^ k
            diff = xor_val - num
            
            if diff > 0:
                diff_sum += diff
                change_count += 1
            min_diff = min(min_diff, abs(diff))
        
        # If we made an odd number of positive changes, we need to revert one
        if change_count % 2 == 1:
            diff_sum -= min_diff
        
        return total_sum + diff_sum
