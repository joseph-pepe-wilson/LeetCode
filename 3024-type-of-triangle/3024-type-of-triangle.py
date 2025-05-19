from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Check if the three sides can form a triangle
        if (
            nums[0] + nums[1] <= nums[2]
            or nums[0] + nums[2] <= nums[1]
            or nums[1] + nums[2] <= nums[0]
        ):
            return "none"

        # Check for equilateral triangle
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"

        # Check for isosceles triangle
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"

        # If none of the above conditions are met, it is scalene
        return "scalene"
