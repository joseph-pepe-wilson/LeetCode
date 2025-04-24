from collections import Counter
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))  # Count distinct elements in the entire array
        count = 0
        left = 0
        freq = Counter()

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while len(freq) == total_unique:  # Valid complete subarray
                count += (
                    len(nums) - right
                )  # All subarrays starting at 'left' and ending at 'right' or beyond are valid
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[
                        nums[left]
                    ]  # Remove element from map if its count drops to zero
                left += 1

        return count
