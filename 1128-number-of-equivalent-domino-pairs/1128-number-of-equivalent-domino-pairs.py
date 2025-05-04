from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        pairs = 0
        
        for a, b in dominoes:
            key = tuple(sorted([a, b]))  # Ensure the representation is consistent
            pairs += count[key]  # Every previous occurrence forms a new valid pair
            count[key] += 1  # Increment count of this particular domino
        
        return pairs
