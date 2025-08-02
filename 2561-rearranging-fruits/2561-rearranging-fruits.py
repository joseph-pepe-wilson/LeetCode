from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        
        total_count = count1 + count2
        for fruit in total_count:
            if total_count[fruit] % 2 != 0:
                return -1  # Impossible to balance
        
        # Find surplus fruits in each basket
        surplus1 = []
        surplus2 = []
        for fruit in total_count:
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                surplus1.extend([fruit] * (diff // 2))
            elif diff < 0:
                surplus2.extend([fruit] * (-diff // 2))
        
        surplus1.sort()
        surplus2.sort(reverse=True)
        
        min_fruit = min(total_count.keys())
        cost = 0
        for f1, f2 in zip(surplus1, surplus2):
            cost += min(2 * min_fruit, min(f1, f2))
        
        return cost
