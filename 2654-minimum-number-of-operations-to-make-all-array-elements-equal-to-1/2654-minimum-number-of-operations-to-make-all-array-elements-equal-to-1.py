from math import gcd
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: If there's already a 1 in the array, count how many operations needed
        count_ones = nums.count(1)
        if count_ones:
            return n - count_ones

        # Step 2: Try to find the shortest subarray with GCD 1
        min_len = float('inf')
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        # Step 3: If no such subarray exists, return -1
        if min_len == float('inf'):
            return -1

        # Step 4: Otherwise, we need (min_len - 1) operations to create a 1,
        # and then (n - 1) more to spread it to the rest
        return (min_len - 1) + (n - 1)