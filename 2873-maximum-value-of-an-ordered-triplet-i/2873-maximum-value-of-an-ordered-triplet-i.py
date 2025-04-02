from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    value = (nums[i] - nums[j]) * nums[k]
                    max_value = max(max_value, value)

        return max_value
