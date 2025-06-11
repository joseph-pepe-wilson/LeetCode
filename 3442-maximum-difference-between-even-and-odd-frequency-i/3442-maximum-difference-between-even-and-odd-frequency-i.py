from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)  # Count character frequencies
        
        odd_freqs = [count for count in freq.values() if count % 2 == 1]
        even_freqs = [count for count in freq.values() if count % 2 == 0]
        
        # Ensure we have both odd and even frequencies before computing
        if odd_freqs and even_freqs:
            return max(odd_freqs) - min(even_freqs)
        
        return 0  # Default return (should not occur given constraints)
