class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = float('inf')  # Set initially to infinity
        n = len(blocks)

        # Iterate through all possible windows of size k
        for i in range(n - k + 1):
            window = blocks[i : i + k]
            operations = window.count('W') # Count the number of white blocks in the current window
            min_operations  = min(min_operations, operations) # Update the minimum operations

        return min_operations