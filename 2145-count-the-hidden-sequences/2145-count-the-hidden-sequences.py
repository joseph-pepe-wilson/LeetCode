from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_value, max_value, current = 0, 0, 0
        
        # Compute the range of possible values for the sequence
        for diff in differences:
            current += diff
            min_value = min(min_value, current)
            max_value = max(max_value, current)
        
        # Determine the valid range for the first element
        range_start = lower - min_value
        range_end = upper - max_value
        
        # Return the count of valid starting values
        return max(0, range_end - range_start + 1)
