class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the array in descending order
        nums.sort(reverse=True)
        
        # Iterate through the sorted array and check for triangle validity
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            # Triangle inequality: sum of two smaller sides must be greater than the largest
            if b + c > a:
                return a + b + c
        
        # If no valid triangle found
        return 0