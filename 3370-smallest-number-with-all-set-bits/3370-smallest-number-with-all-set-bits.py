class Solution:
    def smallestNumber(self, n: int) -> int:
        # Start with 1 and keep shifting left and adding 1 to form numbers like 1, 3, 7, 15, ...
        x = 1
        while x < n:
            x = (x << 1) | 1
        return x