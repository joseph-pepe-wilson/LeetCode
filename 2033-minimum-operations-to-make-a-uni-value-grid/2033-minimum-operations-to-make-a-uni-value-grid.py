from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid to a single list for easier processing
        flattened_grid = [item for row in grid for item in row]
        
        # Calculate the smallest element to use as reference for all operations
        min_value = min(flattened_grid)
        
        # Check if it's possible to make all values equal
        for value in flattened_grid:
            if (value - min_value) % x != 0:
                return -1
        
        # Calculate the target value (median minimizes the number of operations)
        flattened_grid.sort()
        target = flattened_grid[len(flattened_grid) // 2]
        
        # Calculate the total number of operations needed
        operations = 0
        for value in flattened_grid:
            operations += abs(value - target) // x
        
        return operations
