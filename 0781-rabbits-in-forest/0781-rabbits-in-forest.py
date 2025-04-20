from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total_rabbits = 0
        
        for ans, freq in count.items():
            groups = (freq + ans) // (ans + 1)  # Number of groups needed
            total_rabbits += groups * (ans + 1)  # Each group has (ans + 1) rabbits
        
        return total_rabbits
