from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        unique_numbers = set()
        
        # Generate all permutations of three digits
        for num in permutations(digits, 3):
            if num[0] == 0:  # Ensure no leading zeros
                continue
            if num[2] % 2 == 1:  # Ensure the last digit is even
                continue
            unique_numbers.add(num[0] * 100 + num[1] * 10 + num[2])
        
        return sorted(unique_numbers)
