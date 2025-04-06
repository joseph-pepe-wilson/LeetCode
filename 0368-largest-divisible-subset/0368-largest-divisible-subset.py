from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()  # Sorting helps in ensuring every element is only divisible by earlier elements
        n = len(nums)
        dp = [[num] for num in nums]  # Initialize each subset with the number itself
        
        max_subset = []
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:  # Check divisibility condition
                    if len(dp[j]) + 1 > len(dp[i]):  # Update if we find a larger subset
                        dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(max_subset):  # Track the largest subset
                max_subset = dp[i]
        
        return max_subset
