from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # If the array already consists of distinct elements, return 0
        if len(set(nums)) == len(nums):
            return 0

        operations = 0
        while len(set(nums)) != len(nums):
            nums = nums[3:]  # Remove the first three elements
            operations += 1

        return operations

