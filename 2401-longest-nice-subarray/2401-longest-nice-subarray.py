class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 0
        current_bitmask = 0
        left = 0

        for right in range(n):
            while (current_bitmask & nums[right]) != 0:
                current_bitmask ^= nums[left]
                left += 1
            
            current_bitmask |= nums[right]
            max_length = max(max_length, right - left + 1)
        
        return max_length
