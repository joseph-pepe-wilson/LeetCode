class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Calculate the area between the two lines
            width = right - left
            min_height = min(height[left], height[right])
            current_area = width * min_height
            max_water = max(max_water, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water