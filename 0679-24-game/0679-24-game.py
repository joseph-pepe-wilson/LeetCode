from typing import List
import itertools

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # Pick two numbers to operate on
                        a, b = nums[i], nums[j]
                        # Remaining numbers
                        rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        
                        # Try all operations
                        for op in [a + b, a - b, b - a, a * b]:
                            if dfs(rest + [op]):
                                return True
                        # Division (avoid division by zero)
                        if b != 0 and dfs(rest + [a / b]):
                            return True
                        if a != 0 and dfs(rest + [b / a]):
                            return True
            return False
        
        # Try all permutations of the cards
        for perm in itertools.permutations(cards):
            if dfs(list(map(float, perm))):
                return True
        return False
