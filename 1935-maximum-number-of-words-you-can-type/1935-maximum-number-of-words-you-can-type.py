class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)  # Use a set for O(1) lookup
        count = 0
        words = text.split()
        
        for word in words:
            # Check if word contains any broken letter
            if not any(ch in broken_set for ch in word):
                count += 1
                
        return count
