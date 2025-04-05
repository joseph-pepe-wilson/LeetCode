from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index: int, current_xor: int) -> int:
            if index == len(nums):
                return current_xor
            # Include nums[index] in the XOR
            include = dfs(index + 1, current_xor ^ nums[index])
            # Exclude nums[index] from the XOR
            exclude = dfs(index + 1, current_xor)
            return include + exclude
        
        return dfs(0, 0)
