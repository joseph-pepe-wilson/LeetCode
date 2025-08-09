class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A power of two must be positive and have only one bit set in binary
        return n > 0 and (n & (n - 1)) == 0
