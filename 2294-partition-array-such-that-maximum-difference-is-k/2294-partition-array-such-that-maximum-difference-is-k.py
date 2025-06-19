class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        i = 0
        n = len(nums)
        
        while i < n:
            start = nums[i]
            # Extend the current subsequence until the diff > k
            while i < n and nums[i] - start <= k:
                i += 1
            count += 1  # One new subsequence formed
        return count
