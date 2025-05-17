from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
        # Initialize three pointers
        left, mid, right = 0, 0, len(nums) - 1
        
        # Traverse through the list
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
