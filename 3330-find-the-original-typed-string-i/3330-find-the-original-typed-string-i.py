class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        runs = []
        i = 0
        
        # Collect all runs of the same character
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            length = j - i
            if length >= 2:
                runs.append((i, length))
            i = j
        
        # Start with the original string as a valid possibility
        total = 1
        for index, length in runs:
            # We can generate (length - 1) different strings by removing 1 up to (length - 1) of the repeated characters
            total += (length - 1)
        
        return total
