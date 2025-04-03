class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        max_value = 0
        max_diff = 0
        max_num = 0
        
        for num in nums:
            if max_value < max_diff * num:
                max_value = max_diff * num
            
            if max_diff < max_num - num:
                max_diff = max_num - num
   
            if max_num < num:
                max_num = num
            
        return max_value
        
