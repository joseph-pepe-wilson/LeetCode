from bisect import bisect_left
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort potions for binary search
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            # Minimum potion strength needed for success
            min_potion = (success + spell - 1) // spell  # ceil(success / spell)
            # Find the first index in potions where potion >= min_potion
            index = bisect_left(potions, min_potion)
            # All potions from index to end are successful
            result.append(m - index)

        return result