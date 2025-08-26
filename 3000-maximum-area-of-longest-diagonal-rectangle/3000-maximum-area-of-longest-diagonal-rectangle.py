from typing import List
import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0

        for length, width in dimensions:
            diag = math.hypot(length, width)  # Equivalent to sqrt(length**2 + width**2)
            area = length * width

            if diag > max_diag:
                max_diag = diag
                max_area = area
            elif diag == max_diag:
                max_area = max(max_area, area)

        return max_area
