class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Count the number of positive and negative integers
        positive = sum(1 for num in nums if num > 0)
        negative = sum(1 for num in nums if num < 0)
        # Return the maximum of the two counts
        return max(positive, negative)