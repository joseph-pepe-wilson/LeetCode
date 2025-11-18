class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n - 1:
            # If we see a 1, it's the start of a two-bit character (10 or 11)
            if bits[i] == 1:
                i += 2
            else:
                # If we see a 0, it's a one-bit character
                i += 1
        # If we end at the last index, it means the last character is one-bit
        return i == n - 1