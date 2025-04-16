from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        pair_count = 0
        left = 0
        freq = defaultdict(int)
        result = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1
            pair_count += freq[nums[right]] - 1  # Incrementing number of pairs
            
            while pair_count >= k:  # Shrinking the window when valid
                result += len(nums) - right  # All subarrays starting from `left` and ending at `right`
                freq[nums[left]] -= 1
                pair_count -= freq[nums[left]]  # Removing pair contribution
                left += 1
        
        return result
