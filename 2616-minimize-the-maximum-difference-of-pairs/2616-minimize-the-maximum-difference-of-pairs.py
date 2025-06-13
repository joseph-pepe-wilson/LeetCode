from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        # Binary search for the smallest possible maximum difference
        left, right = 0, nums[-1] - nums[0]
        
        def canFormPairs(max_diff):
            count, i = 0, 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 1  # Skip next element to avoid reusing index
                i += 1
            return count >= p
        
        while left < right:
            mid = (left + right) // 2
            if canFormPairs(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
