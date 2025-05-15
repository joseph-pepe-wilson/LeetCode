from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        if n == 0:
            return []
        
        # Initialize the result list with the first element
        result = [words[0]]
        
        # Iterate over the words list, checking the alternating condition
        for i in range(1, n):
            if groups[i] != groups[i - 1]:  # Ensures alternating group values
                result.append(words[i])
        
        return result
