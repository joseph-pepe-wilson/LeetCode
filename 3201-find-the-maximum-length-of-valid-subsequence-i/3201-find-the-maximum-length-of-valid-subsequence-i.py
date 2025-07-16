class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count_even = 0
        count_odd = 0
        alternating_length = 1
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
            
            # For alternating pattern, check if current element differs from previous
            if i > 0 and nums[i] % 2 != nums[i-1] % 2:
                alternating_length += 1
        
        return max(alternating_length, count_even, count_odd)