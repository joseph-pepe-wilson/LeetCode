class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # Helper function to check if a subarray is strictly increasing
        def is_strictly_increasing(start: int) -> bool:
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        
        # Iterate through possible starting indices for the first subarray
        for i in range(n - 2 * k + 1):
            if is_strictly_increasing(i) and is_strictly_increasing(i + k):
                return True
        
        return False