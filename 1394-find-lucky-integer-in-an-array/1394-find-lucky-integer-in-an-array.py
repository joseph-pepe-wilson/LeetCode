from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        # Filter keys where the value equals the key, then return the max or -1 if none
        lucky = [num for num, count in freq.items() if num == count]
        return max(lucky) if lucky else -1
