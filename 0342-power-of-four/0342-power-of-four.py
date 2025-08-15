class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is positive and a power of two
        # Then ensure the only set bit is in the correct position for powers of four
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0
