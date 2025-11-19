class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)  # Convert list to set for faster lookup
        while original in num_set:
            original *= 2
        return original