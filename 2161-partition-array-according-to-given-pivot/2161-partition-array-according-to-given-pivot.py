from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []
        
        # Partition the array into three parts
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num > pivot:
                greater_than_pivot.append(num)
            else:
                equal_to_pivot.append(num)
        
        # Concatenate the parts in the required order
        return less_than_pivot + equal_to_pivot + greater_than_pivot

        