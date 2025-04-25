from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # Base case: to handle subarrays that start from index 0
        count = 0
        curr_cnt = 0

        for num in nums:
            if num % modulo == k:
                curr_cnt += 1
            
            # Compute remainder of curr_cnt % modulo
            remainder = curr_cnt % modulo
            
            # Find matching subarray count
            target_remainder = (remainder - k) % modulo
            count += prefix_count[target_remainder]
            
            # Update prefix frequency
            prefix_count[remainder] += 1

        return count
