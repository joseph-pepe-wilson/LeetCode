class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
    
        def backtrack(counter):
            total_sequences = 0
            for char in counter:
                if counter[char] > 0:
                    total_sequences += 1
                    counter[char] -= 1
                    total_sequences += backtrack(counter)
                    counter[char] += 1
            return total_sequences
    
        return backtrack(Counter(tiles))