from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()  # Sort the array first
        count = 0
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1

            # Move left pointer to find the lowest valid sum
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] + nums[i] < lower:
                    left = mid + 1
                else:
                    right = mid - 1
            start = left

            left, right = i + 1, n - 1

            # Move right pointer to find the highest valid sum
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] + nums[i] > upper:
                    right = mid - 1
                else:
                    left = mid + 1
            end = right

            count += max(0, end - start + 1)  # Count valid pairs

        return count
