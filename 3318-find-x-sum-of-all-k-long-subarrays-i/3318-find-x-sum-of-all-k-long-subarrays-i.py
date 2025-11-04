from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        n = len(nums)
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            freq = Counter(subarray)
            
            # Sort by frequency descending, then by value descending
            sorted_items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            
            # Get the top x elements
            top_x_elements = set()
            for j in range(min(x, len(sorted_items))):
                top_x_elements.add(sorted_items[j][0])
            
            # Sum only the occurrences of top x elements
            x_sum = sum(val for val in subarray if val in top_x_elements)
            result.append(x_sum)
        
        return result