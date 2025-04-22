from collections import Counter
from math import comb

class Solution:
    def idealArrays(self, length: int, max_value: int) -> int:
        MOD = 1_000_000_007
        
        # Step 1: Initialize base frequencies
        total_ways = max_value
        frequency_map = {num: 1 for num in range(1, max_value + 1)}
        
        # Step 2: Expand arrays up to the desired length
        for array_size in range(1, length): 
            new_frequency = Counter()
            
            # Step 3: Extend each valid base value
            for base_value in frequency_map: 
                for multiplier in range(2, max_value // base_value + 1): 
                    # Compute the number of ways to arrange using combinations
                    combinations = comb(length - 1, array_size)
                    total_ways += combinations * frequency_map[base_value]
                    
                    # Store new valid elements in the frequency map
                    new_frequency[multiplier * base_value] += frequency_map[base_value]
            
            # Step 4: Update frequency map for next iteration
            frequency_map = new_frequency
            total_ways %= MOD
        
        return total_ways
