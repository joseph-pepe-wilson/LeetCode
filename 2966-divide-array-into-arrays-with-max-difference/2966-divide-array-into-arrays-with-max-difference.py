from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()  # Sort the array to facilitate grouping
        result = []

        for i in range(0, len(nums), 3):  # Iterate in chunks of 3
            if nums[i + 2] - nums[i] > k:  # If the difference exceeds k, return []
                return []
            result.append([nums[i], nums[i + 1], nums[i + 2]])  # Form a valid triplet

        return result
