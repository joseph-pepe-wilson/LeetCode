class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0, 0, 0]  # to count occurrences of 'a', 'b', and 'c'
        result = 0
        left = 0
        
        for right in range(len(s)):
            # Increment count for the character at position 'right'
            count[ord(s[right]) - ord('a')] += 1
            
            # Check if we have all three characters in the current window
            while all(c > 0 for c in count):
                # Add the number of valid substrings ending at 'right'
                result += len(s) - right
                # Shrink the window from the left
                count[ord(s[left]) - ord('a')] -= 1
                left += 1
                
        return result
