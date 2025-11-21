class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        from collections import defaultdict

        # Store the first and last occurrence of each character
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        result = 0
        for c in set(s):
            if first[c] < last[c]:
                # Collect all unique characters between first and last occurrence of c
                middle_chars = set(s[first[c]+1:last[c]])
                result += len(middle_chars)

        return result